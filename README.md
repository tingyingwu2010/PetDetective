# About
Inspired from a `Lumosity` logic game, I'm trying to find a solution or an approach to solve a Capacitated Vehicle Routing Problem with Pickup and Delivery.

For an illustration, check the following image:

<img src="https://i.imgur.com/x1AGMQX.jpg" alt="alt text" width="300">

In this game, using a rescue car, you need to return all the pets on the map to their homes.
The car has a cargo capacity limit of 4 pets. You can have a maximum of 4 pets in the car at any time.

**The problem: How to find the shortest route to deliver all the pets to their homes?**

# Understanding the problem
As there is no exact algorithm to solve VPR problems and their solutions are NP-hard, before going deeper into VPR technical papers, my first step is to actually take a step back and understand the problem better, with the hope to find a solution.

It was quite obvious I will need a graph to store the map representation. Initially, I visualized every intersection in the map as a graph node. A route would basically be a list of nodes through which the car passes to pick up and deliver the pets to their homes. Some nodes will have to be passed multiple times. And this is a bit of a problem if we want to brute force. There is nothing that can stop the car from going round and round, making redundanct circles.

Going further, I've changed the perspective through which I'm looking at the problem. I moved the abstraction from 'intersections as nodes' to 'items as nodes', where items are the pets, their houses and the car from the map. First, I wrote down all the distances (the shortest ones) between the items on the map. Next, I've put all the items and the distances between them in a graph. As a result, a complete graph was born.

With this abstraction, every node can be traversed only once. No more infinite options. Once you pick up a pet, you don't go back to picking it up again. Even if you'd want to, you can't. Same with the houses, once you deliver a pet to its house, you have nothing to deliver to that house again. When the cars passes through a node, that node can't be passed anymore, it becomes unavailable. The car needs to go node by node until there are no available nodes left.

In this second case, a route is an ordered set of nodes. It contains every single node only once. All that needs to be done, to find the shortest route, is to find the corect order of the nodes that gives the shortest distance. Now this can be brute-forced easily.

# Brute Force Solution
Basically, if the route is an ordered set of nodes, and we have the distance between all the nodes, it's an easy problem to find the correct order of nodes that will give a minimal sum of distances. What makes the brute force solution feasible for this case, is the limited number of nodes. Having a bigger number of nodes, as we will see later, makes this solution impracticle.
It needs to be noted that, for now, finding the shortest distance between two nodes is a quite easy task and remains at the user's discretion.

**To determine the shortest path, generate every possible path and calculate the distance for each of them. The path with the shortest distance is the solution.**


A path is simply a permutation of nodes. The number of all possible permutations is `P(n) = n!`. A map with 4 pets and 4 houses has a total of `40.320` possible paths: `P(8) = 8!= 40.320`. Add just one more pet and you have now a total of `3.628.800` possible paths. This is a lot, but nothing a computer cannot handle. Although, try to imagine a scenario with 20 nodes and we are talking now about a cosmic number of `2.432.902.008.176.640.000` possible paths. I don't even know how to pronounce this number, but it's certainly not an easy task to process this number of paths for a computer either, and we're only talking about 10 pets to be delivered to 10 houses. In real-life, these numbers are usually huge, and thus brute-force solutions are not feasible at all. As we're dealing with a small number of nodes, this is a feasible solution and it can be used to find the shortest path.

#### There are a number of rules to be taken into consideration, when generating the list of paths:
1. **Every path must start with the car's node.** Paths where the car node is in the middle or at the end, are not valid. Filtering out these kind of paths is very easy. We generate all the possible permutations without the car node, and insert the car node as the first node in every path at a later stage.

2. **A pet node has to be traversed before a pet's house node**. In order to deliver a pet to its house, a pet needs to be picked up first and then delivered to its house somewhere later on the path. If this rule is broken, the path is invalid and needs to be filtered out.

3. **Car's cargo capacity has to be kept under limit**. The car has a limited cargo capacity.
Initially, I thought this limitation will break the current solution, but fortunately, I was wrong. From the generated list of paths, we just remove the ones that break this rule - problem solved.


# Performance
It is a brute force algorithm, so it takes some time to find the shortest path for a certain map. On a 13" Macbook Pro, base model, a 5 pets map, without further optimizations, gets solved in about 22 seconds. This is a lot, but it's a viable solution.

## Optimization #1
The permutations list can be easily cut in half.

The permutations that start with any pet's house are invalid from the start. They break the rule #2. Having this list of nodes `['Cat', 'Dog', 'Hedgegog', 'Cat_House', 'Dog_House', 'Hedgehog_House']`, I realized that half of the permutations will start with a pet node, and half of them will start with a house node. And this allowed me to cut out the second half of permutations list.

This optimization decreased the processing time by almost 50%, from 22 seconds to 12 seconds.

I'll be looking forward for other optimizations, but this is what I achieved so far.
