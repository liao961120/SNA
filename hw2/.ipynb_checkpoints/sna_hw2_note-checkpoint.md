---
title: "SNA HW2: Q1 & Q3"
date: "`r format(Sys.Date(), '%B %e, %Y')`"
urlcolor: "blue"
fontsize: 12pt 
geometry: a4paper
linestretch: 1.35
links-as-notes: true
always_allow_html: yes
output:
  bookdown::html_document2:
    number_sections: yes
    toc: yes
    toc_depth: 2
    toc_float:
      collapsed: yes
    css: style.css
---

```{r setup, include=FALSE}
knitr::opts_chunk$set(echo = FALSE, fig.show = 'hold', out.width = '48%')
library(knitr)
```

# Q1

## Data Description: ZACHE

- Edges: Binary. Presence or absence of **interaction**
- Nodes: Members of a university karate club

### Some Questions about ZACHE data

According to [UCINET documentation](https://sites.google.com/site/ucinetsoftware/datasets/zacharykarateclub), the network is undirected but [the given Gephi network](https://www.space.ntu.edu.tw/navigate/s/18264D79D16E4C788436768C4B0EB4C2QQY) is directed.

## Ⅰ


## Ⅱ & Ⅲ (Gephi)

### What centrality measure should be used?

- Degree, Betweeness, Closeness, Eigenvector?

### Network Plots

- Color: Clustering Coefficient (Basic method)
- Node (Text) Size: Centrality Measure

```{r fig.cap='Degree (left); Betweeness (right)'}
include_graphics(c('q1-2-degree_centrality.svg', 'q1-2-betweeness_centrality.svg'))
```


```{r fig.cap='Closeness (left); Eigenvector (right)'}
include_graphics(c('q1-2-closeness_centrality.svg', 'q1-2-eigen_centrality.svg'))
```


# Q3: 104 College Network Data


## Ⅰ & Ⅱ (Gephi)

Metrics (Gephi):

- Degree: `Avg. Weighted Degree` (Since the data has weighted edges)

- Centrality measures (Closeness, Betweenness, Eigenvector): `Network Diameter` & `Eigenvector centrality`


### Network Plots

- Color: Centrality Measure

```{r fig.cap='Degree (left); Weighted Degree (right)'}
include_graphics(c('q3-1-degree.svg', 'q3-1-weighted_degree.svg'))
```


```{r fig.cap='Harmonic Closeness Centrality (left); Closeness Centrality (right)'}
include_graphics(c('q3-1-hm_closeness_centrality.svg', 'q3-1-closeness_centrality.svg'))
```


```{r fig.cap='Betweeness Centrality (left); Eigenvector Centrality (right)'}
include_graphics(c('q3-1-betweeness_centrality.svg', 'q3-1-eigen_centrality.svg'))
```