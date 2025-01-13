"""
Calculate the number 𝑥 obtained by applying the XOR operator between all elements of all subsets of the set 𝐴 = {1, 2, ..., 𝑘} ⊂ ℕ, excluding the empty set.
For example, if 𝑘 = 3, we get 𝑥 = (1)^(2)^(3)^(1^2)^(1^3)^(2^3)^(1^2^3) = 0
(parentheses are used only to highlight the elements of the subsets of A)

"""
# card A = n
# 2^n subsets
# x face parte din 2^k submultimi (adica numarul total de submultimi ale {1, 2, ..., k} - {x})
# numar par 
# xorul da 0

def xor_subsets(n):
    return 0
# complexitate O(1)