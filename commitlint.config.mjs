export default {
  extends: ["@commitlint/config-conventional"],
  rules: {
    "scope-enum": [2, "always", ["calc", "cli", "api", "deps", "ci", "main", "staging", "production"]],
  },
};
