system('python3 clean.py')

library(dplyr)
inschool <- readr::read_csv('1061_inschool.csv')
drop <- readr::read_csv('1061_suspend.csv')



out <- left_join(drop, inschool) %>% 
  mutate(dropRate1061 = (100*drop)/inSchool) %>% 
  select(Id, dropRate1061) %>%
  filter(Id != '中國文學系國際學生學士班')

readr::write_csv(out, '1061_dropoutRate.csv')


# NTU application network pagerank data
#pageranks <- readr::read_csv('ntuApplic_pageranks.csv') %>%
#  select(-ntuapplic_pageranks)

# Add to network_attributes.csv
#ntu_attributes <- readr::read_csv('../network_attributes.csv')
#ntu_attributes <- left_join(ntu_attributes, pageranks)
#ntu_attributes <- left_join(ntu_attributes, out)
#readr::write_csv(ntu_attributes, '../network_attributes.csv')
