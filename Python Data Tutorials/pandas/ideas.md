# Ideas
 1. df = df.apply(lambda x: pd.to_datetime(x, dayfirst=True ), axis=1)
    df.assign(days = lambda x: df.ColB - df.ColA)
    
2. df = pd.DataFrame()
  df['ColA'] = pd.date_range('01/01/2010', periods=5, freq='M')
  df['ColB'] = pd.date_range('01/01/2011', periods=5)
  df['days'] = df.eval('ColA-ColB')
  or df.eval("days=abs(ColA-ColB)", engine='python', inplace=True)
 
3. df.filter(items=['one', 'three'])
   df.filter(regex='e$', axis=1)
   df.filter(like='bbi', axis=0)
   
4. res = df.groupby('year')['country'].nunique().reset_index()
   df['count'] = df.groupby('year')['country'].transform('nunique')
   
5. df.index.name = 'bar'
   df.reset_index().rename(columns={df.index.name:'bar'})
   df.index = df.index.set_names(['foo'])
   
6. cols = cols[-1:] + cols[:-1]

7. import pkg_resources
   pkg_resources.get_distribution("simplegist").version
