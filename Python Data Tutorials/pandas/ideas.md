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
   
8. plt.xticks(np.arange(0, full_data.index.max(), int(full_data.index.max())/20), full_data.ServiceDate.tolist(), rotation=45)
   fig, ax = plt.subplots(ncols=1, nrows=1, figsize=(16, 10))

  # Plot the line
  plt.plot(full_data.index, full_data.AllowedAmount, color='grey', linestyle='dotted', alpha=.5)
  #plt.plot(bench_data.index, bench_data.AllowedAmount, color='black', alpha=.5, linestyle='--')
  #plt.plot(sugbench_data.index, sugbench_data.AllowedAmount, color='green', alpha=.5)
  plt.scatter(full_data.index, full_data.AllowedAmount, s=25, c='black', edgecolor='grey')
  try: plt.scatter(partial_data.index, partial_data.AllowedAmount, s=100, c='red', edgecolor='grey')
  except: pass
  
9. this_dict = {'Checks': ['Date was parsed if needed according to our standards', 2],
    'Types': ['Date', 2],
    'Statuses': ['Parsed', 2],
    'Impact': ['Ready for Load', 2],
    'TabNames': ['No Tab', 2],
    'Results': ['input->2015/01/01 | output->2015-01-01', 2]}
    
    [[value[i] for value in [item[1] for item in this_dict.items()]] for i in range(2)]
    
 10. from datetime import datetime as dt, timedelta as td
     from dateutil.relativedelta import relativedelta as rl
     x = rl(dt.strptime('2017-12-30', '%Y-%m-%d'), dt.strptime('2018-01-01', '%Y-%m-%d'))
     x.months
    
