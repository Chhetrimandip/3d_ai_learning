import time

print("Day five: gradient descent (teaching a machine to learn)")
current_x = 0
target_x = 3.0


learning_rate = 0.1
epochs = 20
print(f"Starting guess: {current_x}")
print(f"Target: {target_x}")
print("-"*30)
for  i in range(epochs):
    loss = (current_x-3) ** 2
    gradient = 2*(current_x-3)
    current_x = current_x-(learning_rate*gradient)
    print(f"Epoch {i+1}: Loss = {loss:.4f} | Gradient = {gradient:.4f} | New x = {current_x:.4f}")
    time.sleep(0.1)

print("-"*30)
print(f"Final result : {current_x:.4f} ")