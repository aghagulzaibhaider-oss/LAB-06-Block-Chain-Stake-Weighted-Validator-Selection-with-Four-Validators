# Lab 06 - Viva Questions and Model Answers

## Q1. What do validators do beyond selection?
Validators check proposed blocks against the protocol rules, communicate votes/attestations, and help the network reach finality. Being selected is only the start: they must also behave honestly and stay online (liveness), or they risk penalties.

## Q2. Does stake replace transaction validation?
No. Having stake gives a validator a chance to be selected, but it is not permission to accept invalid transactions. Every validator must still verify signatures, balances and protocol rules. Blocks with invalid transactions are rejected, and the validator may be penalised.

## Q3. How does this differ from Ethereum PoS?
Ethereum does not use a simple Python weighted lottery. Its consensus uses time slots and epochs, committees, attestations, and protocol-specific finality and slashing logic, with randomness produced by the protocol (RANDAO) rather than a fixed-seed generator. This lab is a toy model of the incentive idea only.

## Extra points that may be asked

**Why is the observed share different from the expected share?**
Selection is random, so there is sampling error. It shrinks as the number of rounds grows (10,000 draws are closer than 2,000), but it is never guaranteed to be exact.

**What does `--slash` do and why does it change the other validators' probabilities?**
It reduces Amina's stake from 50 to 30, so the total becomes 90. Each probability is stake divided by total, so Amina's chance falls to 33.33% and everyone else's rises (Bilal 33.33%, Chen 22.22%, Dalia 11.11%).

**Why use a fixed seed (`random.Random(2026)`)?**
It repeats the same pseudorandom sequence for the same input, which makes marking and verification easy. It is not secure randomness and must not be used in a real PoS protocol.

**What is missing from this toy model?**
Validator duties, attestations, liveness, block finality, adversarial behaviour, real slashing evidence and actual stake deposits.
