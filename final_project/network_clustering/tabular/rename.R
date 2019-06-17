library(dplyr)
lookup <- readr::read_csv('name_lookup.csv')
x = readr::read_csv('ntuNetwork_edges.csv')

copied_tibble = tibble()
for (i in seq_along(x$Source)) {
  idx = which(lookup$college104_id == x$Source[i])
  x$Source[i] = lookup$college104[idx[1]]

  idx2 = which(lookup$college104_id == x$Target[i])
  x$Target[i] = lookup$college104[idx2[1]]
  #if (length(idx) > 1) {
  #  for (j in seq_along(idx)[-1]){
  #    temp = x[i,]
  #    temp$Id[1] = lookup$college104[idx[j]]
  #    copied_tibble = bind_rows(copied_tibble, temp)
  #  }
  #}
}

x %>% arrange(desc(Source)) %>% View()

#x = bind_rows(x, copied_tibble)

readr::write_csv(x, 'ntuNetwork_edges2.csv')
