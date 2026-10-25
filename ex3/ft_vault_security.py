def secure_archive(name: str, action: str = "r", content: str = "",
                   ) -> tuple[bool, str]:
    try:
        if action == "w":
            with open(name, "w") as file:
                file.write(content)
            return (True, "Content successfully written to file")
        else:
            with open(name, "r") as file:
                data = file.read()
            return (True, data)
    except OSError as e:
        return (False, str(e))


def ft_vault_security() -> None:
    print("=== Cyber Archives Security ===")
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))
    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd"))
    print("Using 'secure_archive' to read from a regular file:")
    print(secure_archive("ancient_fragment.txt"))
    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive("archivo_personal.txt", "w", "Este es el archivo"))


if __name__ == "__main__":
    ft_vault_security()
