
import prolog2 

Term = prolog2.Term
e = {}

prolog2.trace = 1
prolog2.unify(Term("[a,b,c]"),{},Term("[A,B,C]"),e)

print("Unifications: %s" % e)

