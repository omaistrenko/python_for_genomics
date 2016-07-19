gene_expr=['lif', 5.16, 0.000138, 7.33]
print str(gene_expr)
gene_expr[1:3]=[6.6] # did not work?
del gene_expr[1]
print gene_expr

gene_expr.extend([22.222, 33.33])
print gene_expr
gene_expr.append('e')
print gene_expr
#gene_expr.pop()
elem=gene_expr.pop()
print elem
print gene_expr

gene_expr.sort()
print gene_expr
gene_expr[:] = []

print gene_expr