# Implementation Plan: Add Hottest Markets Section

## Objective
Add a "Hottest Markets" section to the homepage that displays 3-4 dummy trading markets. Each market card should show a "Launch App" or "Connect Wallet" button on hover.

## Analysis
1. **Location**: The new section should be placed after the "Live protocol metrics" section (`#metrics`) and before the "Dexetera: The Future of Decentralized Trading" section (`#comparison`).

2. **Structure**:
   - Section header with title and description (similar to existing sections)
   - Grid layout for market cards (similar to `.value-grid` but with 4 columns)
   - Each card should contain market information and a hover action button

3. **Styling**:
   - Reuse existing `.card` styles for consistency
   - Add new styles for market-specific elements (price, change percentage)
   - Create hover effects for the action button

4. **Content**:
   - 4 dummy markets with realistic names, prices, and 24h changes
   - Mix of positive and negative changes for visual variety

## Implementation Steps

### HTML Changes
1. Add new section after `#metrics` section
2. Create section header with title and description
3. Create grid container for market cards
4. Add 4 market cards with:
   - Market name
   - Current price
   - 24h change percentage
   - Hover action button

### CSS Changes
1. Add new styles for market grid (4 columns)
2. Add styles for market price and change indicators
3. Add styles for hover action button
4. Ensure responsive design (stack cards on mobile)

## Verification
1. Check desktop layout for proper spacing and alignment
2. Check mobile layout for responsive behavior
3. Verify hover effects work correctly
4. Ensure visual consistency with existing design system

## Confidence Level
9/10 - The implementation reuses existing patterns and styles, making it predictable and consistent with the current design.
