# genetic_algo

## Why use this?

When you have many columns in a dataset and you want to find the subset of the most predictive.

## Dimension reduction? OK, but why not PCA?

Principal Component Analysis is good for some situations but only gives you where there is variance - it doesn't cut through noise. Also, PCA doesn't tell you which columns are most predictive of your output

## Retaining original columns, right... Why not brute force?

If you have 80 columns and you know you only want to keep 20, you would have to brute force over 3.5*10^18 combinations to figure out the optimal solution.

## OK, so it cuts out a lot of unpromissing potential solutions. Doesn't that mean it's probabilistic?

Yes and that's a good thing. If you could execute one billion possible solutions per second, it would still take you 1 billion seconds, it would still take you over 100 years. This algorithm will likely converge on a solution in about an hour on a 2017 bottom of the line laptop.

## Nice. But your code is a mess.

I'm cleaning it up.
