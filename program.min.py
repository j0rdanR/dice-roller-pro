N=int
G=len
D=False
A=print
import random as L,time as F
def C(margin_top,title):B=title;E='\n'*margin_top;C=60;D='='*C;B=f"|    {B.upper()}    |";F=f"{E}{D}\n{B.center(C)}\n{D}\n";A(F)
def E():C(3,'Help!');A('Enter roll in “[quantity]d[sides]” format.\ne.g. Enter 4d6 to roll four six-sided dice.\n\n')
def H(input_string):
	H=input_string;B=H.split('d')
	if G(B)!=2:return D
	try:C=N(B[0]);I=N(B[1])
	except:return D
	if C<1 or I<2:return D
	A(f"\nRolling {H}:\n");E=0;J=[]
	while E<C:
		K=L.randint(1,I);J.append(K)
		if E<15:F.sleep(1/C)
		A(f"Rolled a {K}!");E+=1
	F.sleep(0.5);M(J)
def M(rolls):B=rolls;C(1,'Roll Statistics');D=sum(B);E=round(D/G(B),2);F=min(B);H=max(B);J={'Rolls':B,'Total':D,'Average':E,'Minimum':F,'Maximum':H};A(I(J)+'\n\n')
def I(data):
	A=''
	for (B,C) in data.items():D=f"{B}:{' '*(14-(G(B)+1))}";A+=f"{D}{C}\n"
	return A
def B():
	G=True;C(1,'Dice Roller Pro!');exit=D
	while exit!=G:
		B=input("Enter a roll ('h' for help, 'x' to exit): ");B=B.strip().lower()
		if B=='h':E()
		elif B=='x':C(3,'Goodbye!');exit=G
		elif B!='':
			F=H(B)
			if F==D:A('Invalid input\n')
if __name__=='__main__':
	try:B()
	except Exception as J:A(f"\nA problem occurred when running the program.\nErr info: [{J}]\n")
