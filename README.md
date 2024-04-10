# software_testing_BLE

1) extract the mutation stuff (and pso) to make a c program that takes in file of input seeds and outputs file of mutated seeds
(I'll probably do)

2) write ble test driver to take in these input and run through BLE. Outputs file of input seeds + output
Also needs to handle crashes (prob jovie) 

3) write smth to run BLE output through LCOV to generate coverage data, outputs file of input seeds + coverage data 

4) write a new interesting func to determine which coverage is interesting. This outputs a file of interesting seeds.

And this goes back to 1)

So finally 5) a whole program prob in python to do 1-4 sequentially in a loop that can cutoff based on time or smth