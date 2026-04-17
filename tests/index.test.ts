import { expect, test } from "bun:test";
import { greet } from "../src/index";

test("greet function", () => {
  expect(greet("Developer")).toBe("Hello, Developer!");
});
