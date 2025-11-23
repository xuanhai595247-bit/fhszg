log_file.write(f"--- Log chạy lúc {datetime.now()} ---\n")
        for entry in log_entries:
            log_file.write(entry + "\n")

if __name__ == "__main__":
    # Thay đường dẫn này bằng thư mục mẹ chứa các profile GPM
    BASE_DIR = r"D:"
    patch_runtime_lavamoat(BASE_DIR)

