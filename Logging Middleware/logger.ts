interface Information {
	stack: "backend" | "frontend";
	level: "debug" | "info"| "warn" | "error" | "fatal";
	packages: "cache" | "controller" | "cron_job" | "db" | "domain" | "handler" | "repository" | "route" | "service" | "api" | "component" | "hook" | "page" | "state" | "style" | "auth" | "config" | "middleware" | "utils";
	message: string;
}

const Log = async (stack: Information["stack"], level: Information["level"], package: Information["packages"], message: Information["message"]): Promise<void> => {
	await fetch("http://20.244.56.144/evaluation-service/logs", {
		method: "POST",
		headers: {
			"Content-Type": "application/json",
		},
		body: JSON.stringify({
			"stack": stack,
			"level": level,
			"package": package,
			"message": message
		}),
	});
}