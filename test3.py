import os

def list_directory_contents(path):
    matrix = []

    # Start by adding the top-level directory
    top_level_dir = os.path.basename(path)
    matrix.append([top_level_dir])

    def add_to_matrix(dir_path, row):
        # List all files and subdirectories in the current directory
        for entry in os.listdir(dir_path):
            full_path = os.path.join(dir_path, entry)
            if os.path.isdir(full_path):
                # Add a new row for each subdirectory
                sub_row = [entry]
                add_to_matrix(full_path, sub_row)
                matrix.append(sub_row)  # Append the new row for the subdirectory
            elif os.path.isfile(full_path):
                # If it's a file, add it to the current row
                row.append(entry)

    # Populate the matrix starting from the top-level directory
    add_to_matrix(path, matrix[0])

    return matrix

# Example usage
directory_path = (r"E:\Descargas\Anime 2")# fake path
result_matrix = list_directory_contents(directory_path)

# Print the matrix
for row in result_matrix:
    print(row)



    #esto  list directorio y lo va agregando a una matrix 2d