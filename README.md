# The Ups and Downs of Investing

Liam is heavily invested in the stock market, and has various theories that he uses to predict when the market will rise and when it will fall. Lately, things haven’t been going too well – the only thing rising is his frustration and the only thing falling is his portfolio. He has decided that he needs more data to test his theories with. One characteristic of the market he is particularly interested in is the peaks and valleys of the price of particular stocks. Liam’s definition of a peak is an increasing sequence of at least n consecutive stock prices ending on a peak day, and then a decreasing sequence of at least n consecutive stock prices starting on the peak day (where n depends on the particular stock). A valley is analogous: a decreasing sequence of at least m consecutive stock prices ending on a valley day, and then an increasing sequence of at least m consecutive stock prices starting on the valley day (where again m depends on the particular stock and may differ from n). For example, consider the two weeks of stock prices shown below:

![](chart.png)

If n=2 and m=3 then there are three peaks in this data (with highest points on days 3, 7 and 12) and one valley (with lowest point on day 9). Notice that there is no valley around day 6, since there is not an increasing sequence of length 3 starting at day 6.

Given a set of stock prices and values for n and m, Liam would like to know how many peaks and valleys there are in the data.

# Input
Input starts with a line containing three positive integers s n m, where 1≤s≤1000 is the number of stock prices, and 2≤n,m≤100 are the parameters described above. Following this line will be one or more lines containing a total of s stock prices. All stock prices are non-negative and no two consecutive stock prices will be the same.

# Output
![](sample_IO.png)

Details : [2018 ICPC East-Central NA Regional Practice Contest](https://open.kattis.com/problems/upsanddownsofinvesting)
