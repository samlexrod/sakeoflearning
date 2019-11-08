PROCEDURE [dbo].[usp_SourceToVarchar150_v2](
	@USE_DATABASE VARCHAR(30),
	@CREATE_TABLE_SCHEMA VARCHAR(3),
	@CREATE_TABLE_NAME VARCHAR(80),
	@SOURCE_SCHEMA VARCHAR(3),
	@SOURCE_TABLE_NAMES VARCHAR(MAX),
	@EXECUTE_INSERT INT
	
) AS
/****************************************
* Author: Samuel Rodriguez
* Title: Data Science Analyst
* Description: It takes a list of tables; creates a table defined as varchar(150) based 
*	on the columns of the source tables regardless if the tables have uneven columns; and 
*	inserts the data in the list of tables into the newly created table.
*****************************************/

BEGIN
	DECLARE @CREATE_FIELDS VARCHAR(MAX)
	, @CREATE_COMMAND VARCHAR(MAX)
	, @CREATE_AND_INSERT_COLUMNS_COMMAND VARCHAR(MAX)
	, @INSERT_FIELDS VARCHAR(MAX)
	, @SELECT_INSERT VARCHAR(MAX)
	, @IDX INT = 1
	, @MAX_IDX INT

	IF @EXECUTE_INSERT = 1
		BEGIN
		PRINT 'WITH INSERT EXECUTION'
		END
	ELSE
		BEGIN
		PRINT 'WITHOUT INSERT EXECUTION'
		END

	DECLARE @SOURCE_TABLES AS TABLE(
		TableName VARCHAR(30),
		Idx INT IDENTITY(1, 1)
	)
	INSERT INTO @SOURCE_TABLES 
	SELECT LTRIM(RTRIM(Result))
	FROM AVLN.dbo.fn_SplitStringToTable(@SOURCE_TABLE_NAMES, default, default)

	DECLARE @CREATE_AND_INSERT_COLUMN AS TABLE(
		TABLE_SCHEMA VARCHAR(MAX),
		TABLE_NAME VARCHAR(MAX),
		COLUMN_NAME VARCHAR(MAX),
		ORDINAL_POSITION INT
	)
	SET @CREATE_AND_INSERT_COLUMNS_COMMAND = '
	SELECT 
		TABLE_SCHEMA,
		TABLE_NAME,
		COLUMN_NAME, 
		ORDINAL_POSITION
	FROM ' + @USE_DATABASE + '.INFORMATION_SCHEMA.COLUMNS '
	INSERT INTO @CREATE_AND_INSERT_COLUMN
	EXEC (@CREATE_AND_INSERT_COLUMNS_COMMAND)
	
	PRINT 'Starting Create Statement'
	-- DYNAMIC CREATE STATEMENT

	BEGIN
		SET @CREATE_TABLE_NAME = @USE_DATABASE + '.' + @CREATE_TABLE_SCHEMA + '.' + @CREATE_TABLE_NAME
		SET @CREATE_COMMAND = 'DROP TABLE IF EXISTS ' + @CREATE_TABLE_NAME + CHAR(10) +
			'CREATE TABLE ' + @CREATE_TABLE_NAME + ' (' + CHAR(10)
		SELECT @CREATE_FIELDS = STUFF(
			(SELECT ', ' + COLUMN_NAME + ' VARCHAR(150) NULL' + CHAR(10)
			FROM
				(SELECT 
					*,
					ROW_NUMBER() OVER(PARTITION BY COLUMN_NAME ORDER BY ORDINAL_POSITION) AS ORDER_ID
				FROM @CREATE_AND_INSERT_COLUMN 
				WHERE TABLE_SCHEMA=@SOURCE_SCHEMA 
				AND TABLE_NAME IN (SELECT LTRIM(RTRIM(TableName)) FROM @SOURCE_TABLES)
				AND COLUMN_NAME NOT IN ('RowInsertDateTime', 'RowSourceName', 'IdentityID')
				ORDER BY ORDINAL_POSITION OFFSET 0 ROWS
				) stuffit
			WHERE ORDER_ID = 1
		FOR XML PATH('')), 1, 2, '')
		SET @CREATE_COMMAND = @CREATE_COMMAND + @CREATE_FIELDS + 
			', RowInsertDateTime DATETIME2(7)' + CHAR(10) + 
			', RowSourceName VARCHAR(80)' + CHAR(10) + 
			', IdentityID INT IDENTITY(1,1));'

		PRINT 'Executing Create Statement'
		PRINT @CREATE_COMMAND
		EXEC (@CREATE_COMMAND)
	END

	-- DYNAMIC TABLE INSERT FOR EACH SOURCE TABLE
	SELECT @MAX_IDX = COUNT(1) FROM @SOURCE_TABLES
	WHILE @IDX <= @MAX_IDX
	BEGIN
		SELECT @INSERT_FIELDS = STUFF(
			(SELECT ', ' + COLUMN_NAME + CHAR(10)
			FROM
			--SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA='etl' AND TABLE_NAME = 'v_ClaimValidation'
				(SELECT * 
				FROM @CREATE_AND_INSERT_COLUMN 
				WHERE TABLE_SCHEMA=@SOURCE_SCHEMA 
				AND TABLE_NAME IN (SELECT LTRIM(RTRIM(TableName)) FROM @SOURCE_TABLES)
				AND COLUMN_NAME != 'IdentityID'
				) stuffit
		FOR XML PATH('')), 1, 2, '')
		SET @INSERT_FIELDS = 'INSERT INTO ' + @CREATE_TABLE_NAME + ' (' + @INSERT_FIELDS + CHAR(10) + 
							') ' + CHAR(10) + 
							'SELECT ' + @INSERT_FIELDS + ' FROM ' + @USE_DATABASE + '.' + @SOURCE_SCHEMA + '.' +(SELECT TableName FROM @SOURCE_TABLES WHERE Idx = @IDX)

		PRINT @INSERT_FIELDS

		IF @EXECUTE_INSERT = 1
			BEGIN
			EXEC (@INSERT_FIELDS)
			END

		SET @IDX = @IDX + 1
	END
END
GO
