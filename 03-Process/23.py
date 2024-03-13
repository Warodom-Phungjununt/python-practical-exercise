### Topic : Break/Continue/Pass Statement 2
# Generate a loop which can delete dollar sign
# Then save within the variable hidden_code

secret_code = "H$A$N$NIN$AR$AK$JU$DJ$$$UD"
hidden_code = ""

for c in secret_code:
    if c == '$':
        continue
    
    hidden_code = hidden_code + c

print(hidden_code)