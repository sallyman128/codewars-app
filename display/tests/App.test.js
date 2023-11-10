import React from "react";
import { render, screen, fireEvent, waitFor } from "@testing-library/react";
import "@testing-library/jest-dom/extend-expect"; // For additional matchers

import App from "./App";

// Mock fetchAnalytics function
jest.mock("./api", () => ({
  fetchAnalytics: jest.fn(),
}));

describe("App Component", () => {
  it("renders the component", () => {
    render(<App />);
    expect(screen.getByLabelText(/enter codewars username/i)).toBeInTheDocument();
    expect(screen.getByRole("button", { name: /submit/i })).toBeInTheDocument();
  });

  it("handles form submission successfully", async () => {
    const mockedAnalyticsData = {
      language_scores: { python: 50, javascript: 80 },
    };

    // Mock the fetchAnalytics function to resolve with data
    require("./api").fetchAnalytics.mockResolvedValue(mockedAnalyticsData);

    render(<App />);

    // Simulate user input and form submission
    fireEvent.change(screen.getByLabelText(/enter codewars username/i), {
      target: { value: "testuser" },
    });
    fireEvent.click(screen.getByRole("button", { name: /submit/i }));

    // Wait for the API call and check if the data is rendered
    await waitFor(() => {
      expect(screen.getByText(/language:/i)).toBeInTheDocument();
      expect(screen.getByText(/score:/i)).toBeInTheDocument();
    });
  });

  it("handles form submission with an error", async () => {
    // Mock the fetchAnalytics function to reject with an error
    require("./api").fetchAnalytics.mockRejectedValue(new Error("Invalid Username"));

    render(<App />);

    // Simulate user input and form submission
    fireEvent.change(screen.getByLabelText(/enter codewars username/i), {
      target: { value: "invaliduser" },
    });
    fireEvent.click(screen.getByRole("button", { name: /submit/i }));

    // Wait for the error message to be rendered
    await waitFor(() => {
      expect(screen.getByText(/invalid username/i)).toBeInTheDocument();
    });
  });
});
