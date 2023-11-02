const { exec } = require("child_process");
const { app } = require("./app");

const PORT = process.env.PORT || 3000;

function pythonProcess() {
  const options = {
    maxBuffer: 1024 * 1024 * 10, // Set the maximum buffer size (e.g., 10MB)
  };
  setTimeout(() => {
    exec("python fetch.py", options, (error, stdout, stderr) => {
      if (error) {
        console.error(`exec error: ${error}`);
        return;
      }
      console.log(`stdout: ${stdout}`);
      console.error(`stderr: ${stderr}`);
    });
  }, 0);
}

app.listen(PORT, () => {
  console.log("Server running. Use our API on port: 3000");

  pythonProcess();
});
