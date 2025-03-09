import os
import shutil


def copy_files_recursive(from_path, to_path, remove_dest=False):
	print(f"FROM {from_path} TO {to_path}")
	if remove_dest and os.path.exists(to_path):
		shutil.rmtree(to_path)

	if os.path.exists(from_path):
		if not os.path.exists(to_path):
			os.mkdir(to_path)

		paths = os.listdir(from_path)
		
		for path in paths:

			full_from_path = os.path.join(from_path, path)
			new_to_path = os.path.join(to_path, path)
			print(new_to_path)

			if os.path.isdir(full_from_path):

				os.mkdir(new_to_path)
				copy_files_recursive(full_from_path, new_to_path)
			else:
				shutil.copy2(full_from_path, new_to_path)	

	else:
		raise ValueError("Invalid paths provided")