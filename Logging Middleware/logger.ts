import express from 'express';

const app = express();
app.use(express.json());

interface Information {
	stack: "backend" | "frontend";
	level: "debug" | "info"| "warn" | "error" | "fatal";
	packages: "cache" | "controller" | "cron_job" | "db" | "domain" | "handler" | "repository" | "route" | "service" | "api" | "component" | "hook" | "page" | "state" | "style" | "auth" | "config" | "middleware" | "utils";
	message: string;
}

const Log = async (stack: Information["stack"], level: Information["level"], pkg: Information["packages"], message: Information["message"]): Promise<void> => {
	await fetch("http://20.244.56.144/evaluation-service/logs", {
		method: "POST",
		headers: {
			"Content-Type": "application/json",
		},
		body: JSON.stringify({ stack, level, package: pkg, message }),
	});
}

app.listen(4000, () => console.log("TS Logger running on port 4000"));