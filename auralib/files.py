
import os
#import pathlib
#import pathlib2
import shutil
#from os import getcwd as os_getcwd
#from os import path as os_path
#from os import remove as os_remove
#from os import removedirs as os_removedirs
#from pathlib import Path
#from pathlib2 import Path
#from shutil import move as shutil_move

def copy_file(source_path: str, destination_path: str, force_metadata: bool = False, force_overwrite: bool = False) -> None:
	"""
	Copies a file from source_path to destination_path.

	Args:
		source_path (str): The file path to copy from.
		destination_path (str): The file path to copy to.
		force_metadata (bool, optional): Whether to force copying metadata from the source file. Defaults to False.
		force_overwrite (bool, optional): Whether to force overwriting the destination file. Defaults to False. Warning: If force_metadata is also True, this will delete the destination file before copying, even if copying fails.
	"""
	try:
		if is_file(source_path):
			if not force_metadata:
				if not force_overwrite:
					shutil.copy(source_path, destination_path)
				else:
					shutil.copy(source_path, destination_path, copy=True)
			else:
				try:
					shutil.copy2(source_path, destination_path)
				except FileExistsError:
					if not force_overwrite:
						print(f"WARNING: '{source_path}' already exists at '{destination_path}'. Skipped copying file. Set the argument 'force_overwrite' to 'True' to force overwrite.")
					else:
						delete_file(destination_path)
						shutil.copy2(source_path, destination_path)
		else:
			raise FileNotFoundError(f"'{source_path}' does not exist or is not a file.")
	except Exception as e:
		print(f"ERROR: Error while trying to copy file '{source_path}' to '{destination_path}': {e}")

def copy_folder(source_path: str, destination_path: str, force_metadata: bool = False, force_overwrite: bool = False) -> None:
	"""
	Copies a directory from source_path to destination_path.

	Args:
		source_path (str): The file path to copy from.
		destination_path (str): The file path to copy to.
		force_metadata (bool, optional): Whether to force copying metadata from the source file. Defaults to False.
		force_overwrite (bool, optional): Whether to force overwriting the destination file. Defaults to False. Warning: If force_metadata is also True, this will delete the destination directory before copying, even if copying fails.
	"""
	try:
		if is_folder(source_path):
			if force_metadata:
				try:
					shutil.copy2(source_path, destination_path)
				except FileExistsError:
					if force_overwrite:
						delete_folder(destination_path)
						shutil.copy2(source_path, destination_path)
					else:
						print(f"WARNING: '{source_path}' already exists at '{destination_path}'. Skipped copying file. Set the argument 'force_overwrite' to 'True' to force overwrite.")
			else:
				if force_overwrite:
					shutil.copy(source_path, destination_path, copy=True)
				else:
					shutil.copy(source_path, destination_path)
		else:
			raise FileNotFoundError(f"'{source_path}' does not exist or is not a folder.")
	except Exception as e:
		print(f"ERROR: Error while trying to copy folder '{source_path}' to '{destination_path}': {e}")

#def copy_from_path(source_path: str, destination_path: str, force_metadata: bool = False, force_overwrite: bool = False, type: str | None = None) -> None:
#	"""
#	valid values for type: None, "file", "folder"
#	"""
#	try:
#		if type == None:
#			if is_file(source_path):
#				copy_file(source_path, destination_path, force_metadata=force_metadata, force_overwrite=force_overwrite)
#			elif is_folder(source_path):
#				copy_folder(source_path, destination_path, force_metadata=force_metadata, force_overwrite=force_overwrite)
#			else:
#				raise FileNotFoundError(f"'{source_path}' does not exist or is not a file or folder.")
#		elif type == "folder":
#			if not is_folder(source_path):
#				raise FileNotFoundError(f"'{source_path}' does not exist or is not a folder.")
#			else:
#				copy_folder(source_path, destination_path, force_metadata=force_metadata, force_overwrite=force_overwrite)
#		elif type == "file":
#			if not is_file(source_path):
#				raise FileNotFoundError(f"'{source_path}' does not exist or is not a file.")
#			else:
#				copy_file(source_path, destination_path, force_metadata=force_metadata, force_overwrite=force_overwrite)
#		else:
#			raise ValueError(f"Invalid type '{type}'.")
#	except Exception as e:
#		print(f"ERROR: Error while trying to copy '{source_path}' to '{destination_path}': {e}")

def delete_file(file_path: str) -> None:
	"""
	Deletes a file.

	Args:
		file_path (str): The file path to delete.
	"""
	try:
		os.remove(file_path)
	except Exception as e:
		print(f"ERROR: Error while trying to delete file '{file_path}': {e}")

def delete_folder(file_path: str) -> None:
	"""
	Deletes a directory.

	Args:
		file_path (str): The file path to delete.
	"""
	try:
		os.removedirs(file_path)
	except Exception as e:
		print(f"ERROR: Error while trying to delete folder '{file_path}: {e}")

#def delete_from_path(file_path: str) -> None:
#	try:
#		if os.path.isfile(file_path):
#			delete_file(file_path)
#		elif os.path.isdir(file_path):
#			delete_folder(file_path)
#		else:
#			raise FileNotFoundError(f"ERROR: '{file_path}' does not exist.")
#	except Exception as e:
#		print(f"ERROR: Error while trying to delete file '{file_path}': {e}")

def get_base_path(file_path: str) -> str:
	"""
	Gets the base path (full path except the last component) of the specified file path.

	Args:
		file_path (str): The file path to get the base path of.

	Returns:
		str: The base path of the specified file path.
	"""
	try:
		return os.path.dirname(file_path)
	except Exception as e:
		print(f"ERROR: Error while trying to get base path of '{file_path}': {e}")

def get_file_extension(file_path: str, include_dot: bool = False) -> str:
	"""
	Gets the file extension of the specified file path.

	Args:
		file_path (str): The file path to get the extension of.
		include_dot (bool, optional): Whether to include the dot in the returned extension. Defaults to False.

	Returns:
		str: The extension of the specified file path.
	"""
	try:
		if include_dot:
			return os.path.splitext(file_path)[1]
		else:
			return strip_dot(os.path.splitext(file_path)[1])
	except Exception as e:
		print(f"ERROR: Error while trying to get file extension of '{file_path}': {e}")

def get_file_name(file_path: str, include_extension: bool = True) -> str:
	"""
	Gets the file name of the specified file path.

	Args:
		file_path (str): The file path to get the name of.
		include_extension (bool, optional): Whether to include the extension in the returned name. Defaults to True.

	Returns:
		str: The name of the specified file path.
	"""
	try:
		if include_extension:
			return os.path.basename(file_path)
		else:
			return os.path.splitext(os.path.basename(file_path))[0]
	except Exception as e:
		print(f"ERROR: Error while trying to get file name of '{file_path}': {e}")

def get_files_with_extension(file_path: str, extension: str | list[str] | tuple[str]) -> list[str]:
	"""
	Searches for files with the specified extension in the specified folder.

	Args:
		file_path (str): The path to the folder to search in.
		extension (str | list[str] | tuple[str]): The extension to search for.

	Returns:
		list[str]: A list of file paths with the specified extension.
	"""
	try:
		paths: list[str] = []
		for dirpath, _, filenames in os.walk(file_path):
			for filename in filenames:
				if has_extension(filename, strip_dot(extension)):
					paths.append(os.path.join(dirpath, filename))
				#file = os.path.join(dirpath, filename)
				#if has_extension(file, extension, include_dot):
				#	paths.append(file)
		return paths
	except Exception as e:
		print(f"ERROR: Error while trying to get files with extension '{extension}' in '{file_path}': {e}")

def get_root_path() -> str:
	"""
	Gets the root path of the current working directory.

	Returns:
		str: The root path of the current working directory.
	"""
	try:
		return os.getcwd()
	except Exception as e:
		print(f"ERROR: Error while trying to get current working directory: {e}")

def has_extension(file_path: str, extensions: str | list[str] | tuple[str]) -> bool:
	"""
	Checks if the file at the specified file path has the specified extension.

	Args:
		file_path (str): The file path to check.
		extensions (str | list[str] | tuple[str]): The extension to check for.

	Returns:
		bool: True if the file path has the specified extension, False otherwise.
	"""
	try:
		extensions: tuple[str] | list[str] = (extensions) if type(extensions) == str else extensions
		extensions = tuple(strip_dot(extension) for extension in extensions)
		return get_file_extension(file_path, False) in extensions
	except Exception as e:
		print(f"ERROR: Error while trying to check if '{file_path}' ends with with extension '{extensions}': {e}")

def is_file(file_path: str) -> bool:
	"""
	Checks if the specified file path is an existing file.

	Args:
		file_path (str): The file path to check.

	Returns:
		bool: True if the file path is a file, False otherwise.
	"""
	try:
		return os.path.isfile(file_path)
	except Exception as e:
		print(f"ERROR: Error while trying to check if '{file_path}' is a file: {e}")

def is_file_with_extension(file_path: str, extensions: str | list[str] | tuple[str]) -> bool:
	"""
	Checks if the specified file path is an existing file with the specified extension.

	Args:
		file_path (str): The file path to check.
		extensions (str | list[str] | tuple[str]): The extension to check for.

	Returns:
		bool: True if the file path is a file with the specified extension, False otherwise.
	"""
	return False if not is_file(file_path) or not has_extension(file_path, extensions) else True

def is_folder(file_path: str) -> bool:
	"""
	Checks if the specified file path is an existing directory.

	Args:
		file_path (str): The file path to check.

	Returns:
		bool: True if the file path is a directory, False otherwise.
	"""
	try:
		return os.path.isdir(file_path)
	except Exception as e:
		print(f"ERROR: Error while trying to check if '{file_path}' is a folder: {e}")

def move_files(source_path: str | list[str] | tuple[str], destination_path: str, force_overwrite: bool = False) -> None:
	try:
		#output_to_dir: bool = True if os.path.isdir(destination_path) else False
		if type(source_path) in (tuple, list):
			#destination = os.path.join(os.path.dirname(source_path), destination_path) if destination_path == os.path.basename(destination_path) else destination_path
			#if os.path.isfile(destination) and not force_overwrite:
				#raise FileExistsError
			for source in source_path:
				if os.path.isdir(source):
					raise IsADirectoryError(f"ERROR: 'move_files()' does not support moving directories. '{source}' is a directory.")
				if os.path.isfile(destination_path):
					raise NotADirectoryError(f"ERROR: If source_path is a list or tuple, then destination_path must be a directory path. '{destination_path}' is a file.")
				file_name = get_file_name(source)
				try:
					os.makedirs(destination_path, exist_ok=True)
					shutil.move(source, destination_path)
					print(f"INFO: '{file_name}' moved to '{destination_path}'")
				except shutil.Error as Error:
					if force_overwrite:
						print(f"WARNING: '{file_name}' already exists at '{destination_path}'. Deleting file and trying again.")
						delete_file(destination_path)
						shutil.move(source, destination_path)
						print(f"INFO: Moved file:'{file_name}' changed to '{destination_path}'")
					else:
						raise Error(f"WARNING: '{file_name}' already exists at '{destination_path}'. Skipped moving file. Set the argument 'force_overwrite' to 'True' to force overwrite.")
		else:
			if os.path.isdir(source_path):
				raise IsADirectoryError(f"ERROR: 'move_files()' does not support moving directories. '{source_path}' is a directory.")
			file_name = get_file_name(source_path)
			try:
				shutil.move(source_path, destination_path)
				print(f"INFO: '{file_name}' moved to '{destination_path}'")
			except shutil.Error as Error:
				if force_overwrite:
					print(f"WARNING: '{file_name}' already exists at '{destination_path}'. Deleting file and trying again.")
					delete_file(destination_path)
					shutil.move(source_path, destination_path)
					print(f"INFO: '{file_name}' moved to '{destination_path}'")
				else:
					raise Error(f"WARNING: '{file_name}' already exists at '{destination_path}'. Skipped moving file. Set the argument 'force_overwrite' to 'True' to force overwrite.")
	except Exception as e:
		print(f"ERROR: Error while trying to move file '{source_path}' to '{destination_path}': {e}")

def move_folders(source_path: str | list[str] | tuple[str], destination_path: str) -> None:
	if type(source_path) in (tuple, list):
		for source in source_path:
			try:
				if os.path.isdir(source):
					raise NotADirectoryError(f"ERROR: 'move_folders()' does not support moving files. '{source}' is a file.")
				folder_name = os.path.basename(source)
				shutil.move(source, destination_path)
				print(f"INFO: Moved folder: '{folder_name}' changed to '{os.path.join(destination_path, folder_name)}'")
			except Exception as e:
				print(f"ERROR: Error while trying to move folder '{source}' to '{destination_path}': {e}")
	else:
		try:
			if os.path.isfile(source_path):
				raise NotADirectoryError(f"ERROR: 'move_folders()' does not support moving files. '{source_path}' is a file.")
			folder_name = os.path.basename(source_path)
			shutil.move(source_path, destination_path)
			print(f"INFO: Moved folder: '{folder_name}' changed to '{os.path.join(destination_path, folder_name)}'")
		except Exception as e:
			print(f"ERROR: Error while trying to move folder '{source_path}' to '{destination_path}': {e}")

def rename_file(file_path: str, new_name: str) -> None:
	""""
	Renames a file.

	Args:
		file_path (str): The path to the file to rename.
		new_name (str): The new name for the file.
	"""
	try:
		if os.path.isdir(file_path):
			raise IsADirectoryError(f"ERROR: 'rename_file()' does not support renaming directories. '{file_path}' is a directory.")
		if new_name == get_file_name(new_name):
			destination_path = os.path.join(get_base_path(file_path), new_name)
		else:
			if os.path.isdir(new_name):
				raise IsADirectoryError(f"ERROR: A new file name much be specified. '{new_name}' is a directory.")
			destination_path = new_name
		shutil.move(file_path, destination_path)
		print(f"INFO: Renamed file: '{file_path}' changed to '{destination_path}'")
		#print(f"INFO: Renamed file: '{file_path}' renamed to '{new_name}'")
		#print(f"INFO: Renamed file: '{get_file_name(file_path)}' renamed to '{new_name}'")
	except Exception as e:
		print(f"ERROR: Error while trying to rename file '{file_path}' to '{new_name}': {e}")

def rename_folder(file_path: str, new_name: str) -> None:
	"""
	Renames a directory.

	Args:
		file_path (str): The path to the directory to rename.
		new_name (str): The new name for the directory.
	"""
	try:
		if os.path.isfile(file_path):
			raise NotADirectoryError(f"ERROR: 'rename_folder()' does not support renaming files. '{file_path}' is a file.")
		if new_name == os.path.basename(new_name):
			destination_path = os.path.join(get_base_path(file_path), new_name)
		else:
			if os.path.isfile(new_name):
				raise NotADirectoryError(f"ERROR: A new directory name much be specified. '{new_name}' is a file.")
			destination_path = new_name
		shutil.move(file_path, destination_path)
		print(f"INFO: Renamed folder: '{file_path}' changed to '{destination_path}'")
		#print(f"INFO: Renamed folder: '{file_path}' renamed to '{new_name}'")
		#print(f"INFO: Renamed folder: '{os.path.basename(file_path)}' renamed to '{new_name}'")
	except Exception as e:
		print(f"ERROR: Error while trying to rename folder '{file_path}' to '{new_name}': {e}")

def strip_dot(extension: str | list[str] | tuple[str]) -> str | list[str] | tuple[str]:
	"""
	Strips the dot ('.') from the beginning of an extension if it exists.

	Args:
		extension (str | list[str] | tuple[str]): The extension to strip the dot from.
	"""
	try:
		if type(extension) in (tuple, list):
			clean_extension: list = []
			for e in extension:
				e = e.lstrip('.')
				clean_extension.append(e)
			if type(extension) == tuple:
				return tuple(clean_extension)
			else:
				return clean_extension
		else:
			return extension.lstrip('.')
	except Exception as e:
		print(f"ERROR: Error while trying to strip dot from '{extension}': {e}")

def test() -> None:
	file_path = "C:\\Code\\Projects\\My Projects\\aurapy\\aura_files.py"
	#file_path = "aura_files.py"
	extensions = [".py", ".txt"]
	print(f"get_file_extension('{file_path}') = '{get_file_extension(file_path, True)}'")
	print(f"is_file('{file_path}') = '{is_file(file_path)}'")
	print(f"is_file_with_extension('{file_path}', '{extensions}') = '{is_file_with_extension(file_path, extensions)}'")
	print(f"is_folder('{file_path}') = '{is_folder(file_path)}'")
	#test = 
	#print(test)

if __name__ == "__main__":
	test()
