import pybel as ob


def main():
	mol = ob.readstring("smi", "CCCC")
	print(mol.molwt)
	print(len(mol.atoms))


if __name__=="__main__":
	main()
