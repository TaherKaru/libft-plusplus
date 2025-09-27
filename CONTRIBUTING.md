# Contributing to libftplusplus

Thank you for your interest in contributing to **libftplusplus**! By participating, you agree to follow our code of conduct and help keep the project high-quality and maintainable.

## 📝 How to Contribute

1. **Fork the repository**  
   Create your own copy of the project by clicking “Fork” on GitHub.

2. **Clone your fork**  
   ```bash
   git clone git@github.com:your-username/libftplusplus.git
   cd libftplusplus

3. **Create a new branch**
   Use descriptive names for your branches:

   ```bash
   git checkout -b feature/my-new-function
   ```

4. **Make your changes**

   * Follow the existing **coding style**.
   * Write **clear, meaningful commit messages**.
   * Add **unit tests** in the `tests/` folder if you add new functionality.

5. **Run tests**
   Make sure everything passes before submitting a PR:

   ```bash
   make re
   ./tests/run_tests   # adjust if using your own test runner
   ```

6. **Push your branch**

   ```bash
   git push origin feature/my-new-function
   ```

7. **Open a Pull Request**

   * Explain the purpose of your changes clearly.
   * Reference any related issues.
   * Wait for review and feedback.

---

## ⚡ Guidelines

* Keep commits **atomic** (one change per commit).
* Document all **public functions** in `include/libftplusplus.h`.
* Respect the **branching model**: `main` = stable, `dev` = ongoing development.
* Only push tested code to `dev` or create PRs for `main`.


Thank you for helping make **libftplusplus** better! 🚀
