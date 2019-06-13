library(dplyr)
lookup <- readr::read_csv('name_lookup.csv')
x = readr::read_csv('transfer_netSEPart.csv')

for (i in seq_along(x$X1)) {
  x$X1[i] = lookup$college104[lookup$transfer == x$X1[i]]
}

readr::write_csv(x, 'transfer_netSEPart2.csv')
