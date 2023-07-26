# What is the complexity of your algorithm (in big O notation)?

- For each offensive ship (there are n/2 of them), we look for the nearest unpaired support ship. For each offensive ship, we potentially go through all the support ships (there are also n/2 of them), which gives a complexity of O((n/2) * (n/2)) = O(n^2 / 4), which is equivalent to O(n^2)

- Then, for each pair formed (there are n/2 of them), we calculate the new position of the support ship, which is an operation in O(1), so this part of the algorithm is in O(n).

__The total complexity of the algorithm is therefore O(n^2).__


# How would you improve your algorithm?
- To improve the relevance of the solution, we could consider moving the offensive ship as well. This is expected to be a faster solution because let's imagine there's a distance of 10 between the offensive ship and its support, with the current algorithm if the ships take one turn to move by 1, it would take 10 turns, whereas if both move closer it would only take 4 or 5 turns. However, the resulting code would be less readable and we would have to think about exceptions. For example, an exception could be when the meeting point of one pair is the same as another. In terms of algorithmic complexity, moving the offensive ships could potentially increase the complexity.

- Other possible improvements:

    - __Parallelization__: If the number of ships is very large, the algorithm could be parallelized to speed up the pairing and moving process. This would be particularly effective on multi-core or distributed systems.

    - __Use of a more sophisticated pairing algorithm__: Currently, the algorithm simply pairs each offensive ship with the nearest unpaired support ship. This could lead to situations where some ships are much further from their partner than others. A better approach might be to use a more sophisticated pairing algorithm, like the Gale-Shapley algorithm.-

# How would your adapt your algorithm to three dimensions? How would that affect the complexity?
- Position generation: Instead of generating positions (x, y), we would have to generate positions (x, y, z).

- Distance calculation: The distance calculation becomes (sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2))

- Movement of ships: When the ships move, we have to consider all three dimensions.

- As for the complexity of the algorithm, searching for the nearest support ship becomes more costly. The complexity becomes O(n^3).

