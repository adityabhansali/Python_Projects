import random
import string
def isSizeInRange(num):
	if(num >= 8 and num <= 16):
		return True
	else:
		print("Not in Range password should be under 8 to 16 size only.")
		print("Re-enter Password:") 
		main()
def sizeAcceptor():
	while(True):
		num = int(input("Enter Size of the password that you want to create?"))
		if(isSizeInRange(num)):
			print("Password Size Accepted:")
			return num
		else:
			print("Error in Accepting response:")
			break
def password_random(pass_size):
	str=string.ascii_lowercase
	return ''.join(random.choice(str) for i in range(pass_size))
def main():
	pass_size=sizeAcceptor()
	password = password_random(pass_size)
	print("Your password is "+password)
main()