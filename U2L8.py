df = pd.DataFrame({'Bull': [.9, .15, .25], 
                   'Bear': [.075, .8, .25],
                   'Stagnant': [.025, .05, .5]
                  }, 
                  index=["Bull", "Bear", "Stagnant"])

# What are the transition probabilities after 1 transition?

print(df)

#            Bear  Bull  Stagnant
# Bull      0.075  0.90     0.025
# Bear      0.800  0.15     0.050
# Stagnant  0.250  0.25     0.500

# What are the transition probabilities after 2 transitions? 
df2=df
print('After two transitions:')
print(df.dot(df2))

n = 3 # number of iterations or dot products
df2=df
for i in range(n): df2 = df2.dot(df)
print('Transition matric after' + str(n) + 'transitions:')
print(df2)
