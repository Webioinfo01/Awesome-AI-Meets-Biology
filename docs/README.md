# Local Development Setup

If you are opening `index.html` locally (e.g., by double-clicking the file), you might encounter issues with loading `data.json` due to browser security restrictions (CORS).

To properly view and test the `index.html` file and its data dependencies locally, it is recommended to serve the files using a simple HTTP server.

## Steps to Run Locally:

1.  **Open your terminal.**
2.  **Navigate to the `docs` directory:**
    ```bash
    cd docs
    ```
3.  **Start the Python HTTP server:**
    ```bash
    python -m http.server
    ```
    (If you are using Python 2, use `python -m SimpleHTTPServer` instead.)
4.  **Access in your browser:** Open your web browser and navigate to `http://localhost:8000`. Then, click on `index.html` to view the page.

To stop the server, press `Ctrl + C` in your terminal. 

# AweAgent Updater
Here are some examples of how to use the `aweagent updater` command:

-   **Generate RSS Feed:** 
    ```bash
    aweagent updater --mode rss --archive-file docs/data.json --rss-path docs/rss.xml
    ```

-   **Update README from Archive:** 
    ```bash
    aweagent updater --mode readme --archive-file docs/data.json --readme-path README.md --no-backup
    ```

-   **Interactively Add a Record:** 
    ```bash
    aweagent updater --mode new_interactive --archive-file docs/data.json
    ``` 