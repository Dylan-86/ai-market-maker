# Implementation Plan: Invert Mobile Order of Hero Elements

## Objective
On mobile viewports, the `aside.hero-visual` currently appears before `div.hero-copy`. The goal is to invert this order so that `div.hero-copy` appears first on mobile.

## Analysis
1. The current CSS applies `order: -1` to `.hero-visual` at the `900px` breakpoint, which causes it to appear first.
2. The `.hero-copy` element does not have an explicit `order` property, so it defaults to `0`.
3. To invert the order, we can either:
   - Remove the `order: -1` from `.hero-visual`, or
   - Set `order: 1` on `.hero-visual` and `order: 0` on `.hero-copy` (explicitly)

## Solution
Remove the `order: -1` property from `.hero-visual` in the `@media (max-width: 900px)` media query. This will allow the natural DOM order to take effect, where `.hero-copy` appears before `.hero-visual`.

## Implementation Steps
1. Locate the `@media (max-width: 900px)` media query in `styles.css`.
2. Remove the line `order: -1;` from the `.hero-visual` rule.
3. Verify the change by checking the mobile layout.

## Verification
- Test the layout on mobile viewports to ensure `.hero-copy` appears before `.hero-visual`.
- Ensure the change does not affect desktop layouts.

## Confidence Level
10/10 - This is a straightforward CSS change with predictable results.
