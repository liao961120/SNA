library(dplyr)
lookup <- readr::read_csv('name_lookup.csv')
x = readr::read_csv('job_stability.csv')

copied_tibble = tibble()
for (i in seq_along(x$Id)) {
  idx = which(lookup$work104 == x$Id[i])
  x$Id[i] = lookup$college104[idx[1]]
  if (length(idx) > 1) {
    for (j in seq_along(idx)[-1]){
      temp = x[i,]
      temp$Id[1] = lookup$college104[idx[j]]
      copied_tibble = bind_rows(copied_tibble, temp)
    }
  }
}

x = bind_rows(x, copied_tibble)

readr::write_csv(x, 'job_stability2.csv')
