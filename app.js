const express = require("express");
const logger = require("morgan");
const cors = require("cors");

require("dotenv").config();
const bodyParser = require("body-parser");
const app = express();
const dataRouter = require("./router");

const formatsLogger = app.get("env") === "development" ? "dev" : "short";

app.use(logger(formatsLogger));
app.use(cors());
app.use(express.json());
app.use(bodyParser.text()); // Middleware to parse text data


app.use(express.static("public"));
app.use("/api", dataRouter);

app.use((req, res) => {
  res.status(404).json({ message: "Not found, wrong URL" });
});

app.use((err, req, res, next) => {
  const { status = 500, message = "Server error" } = err;
  res.status(status).json({ ResponseBody: { message } });
});

module.exports = { app };
