library(dplyr)
lookup <- readr::read_csv('name_lookup.csv')
x2 = readr::read_csv('../raw_network_data/transfer_edges.csv')

for (i in seq_along(x$source)) {
  x$source[i] = lookup$college104[lookup$transfer == x$source[i]]
  x$target[i] = lookup$college104[lookup$transfer == x$target[i]]
}

readr::write_csv(x, '../raw_network_data/transfer_edges2.csv')
