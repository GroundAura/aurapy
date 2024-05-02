# aura.py | Aura's Python Function Library

aura.py is mostly a way for me to reuse some functions I use a lot in my projects, and a learning exercise. Feel free to use these for your own projects if you want though (see license).

## Modules & Functions

### `aura_cmd.py`

`run_command()` runs a command line command. Options to use shell and print output.

```py
run_command(
  command: str | list[str],
  print_output: bool = False,
  use_shell: bool = False
) -> None
```

### aura_config.py

`read_config()` reads a configuration file in INI format and returns it as a dictionary, with data types formatted according to the first character of keys (`b`: boolean, `i`: integer, `f`: float, `s`: string). It allows you to use a variable value to start file paths at the current working directory; option keys must begin or end with specified strings. It also has options to preserve/ignore the case of keys, enable debug logging, and specify custom valid values for boolean and current working directory variables.

```py
read_config(
  file_path: str,
  preserve_keys_case: bool = False,
  debug: bool = False,
  root_dir_key: tuple[str] | str = ("PATH", "Path", "path", "sPATH", "sPath", "spath"),
  root_dir_value: str = "[ROOT]",
  true_values: tuple[str] | str = ("TRUE", "True", "true", "T", "t", "1"),
  false_values: tuple[str] | str = ("FALSE", "False", "false", "F", "f", "0")
) -> dict[str, dict[str]]
```

### aura_files.py

`delete_file()` deletes a file.

```py
delete_file(
  file_path: str | tuple[str]
) -> None
```

`delete_folder()` deletes a directory.

```py
delete_folder(
  file_path: str | tuple[str]
) -> None
```

`get_base_path()` gets only the directory elements from a path to a file. Eg: `c:\example\folders`

```py
get_base_path(
  file_path: str
) -> str
```

`get_file_name()` gets only the file element from a path. Includes the extension by default, but you can disable this. Eg: `file.txt`, `file`

```py
get_file_name(
  file_path: str
  include_extension: bool = True
) -> str
```

`get_file_extension()` gets only the file extension from a path to a file. Includes the `.` by default, but you can disable this. Eg: `.txt`, `txt`

```py
get_file_extension(
  file_path: str
  include_dot: bool = True
) -> str
```

`get_root_path()` gets the current working directory path.

```py
get_root_path() -> str
```

`has_extension()` checks if a path or string ends with an extension or one of a list/tuple of extensions.

```py
has_extension(
  file_path: str,
  extensions: str | list[str] | tuple[str]
) -> bool
```

`is_file()` checks if a file exists at a path.

```py
is_file(
  file_path: str
) -> bool
```

`is_file_with_extension()` checks in a file exists at a path and ends with an extension or one of a list/tuple of extensions.

```py
is_file_with_extension(
  file_path: str,
  extensions: str | list[str] | tuple[str]
) -> bool
```

`is_folder()` checks if a folder exists at a path.

```py
is_folder(
  file_path: str
) -> bool
```

`move_files()` moves a single file or a list/tuple of files into a specified folder. If moving a single file you can specify a file name, allowing renaming, however this is not supported with multiple files.

```py
move_files(
  source_path: str | list[str] | tuple[str],
  destination_path: str,
  force_overwrite: bool = False
) -> None
```

`move_folders()` moves a single folder or a list/tuple of folders into a specified folder.

```py
move_folders(
  source_path: str | list[str] | tuple[str],
  destination_path: str
) -> None
```

`rename_file()` renames a single file to a new name, including extension. Optionally, you may specify a full file path to move the file as well.

```py
rename_file(
  file_path: str,
  new_name: str
) -> None
```

`rename_folder()` renames a single folder to a new name. Optionally, you may specify a full file path to move the folder as well.

```py
rename_folder(
  file_path: str,
  new_name: str
) -> None
```

### aura_json.py

`escape_json_string()` replaces common dangerous characters in a string with their json-escaped equivalents, allowing them to be used in json files.

```py
escape_json_string(
  string: str
) -> str
```

### aura_skyrim.py

`is_bethesda_plugin()` checks if a string ends in `.esp`, `.esm`, or `.esl`. By default it also checks if the string is a path to a file.

```py
is_bethesda_plugin(
  file_path: str,
  check_if_file: bool = True
) -> bool
```

### aura_xml.py

`escape_xml_string()` replaces common dangerous characters in a string with their xml-escaped equivalents, allowing them to be used in xml files.

```py
escape_xml_string(
  string: str, fomod: bool = False
) -> str
```

## License

[Clear BSD](https://github.com/GroundAura/aurapy/blob/main/LICENSE.txt)
