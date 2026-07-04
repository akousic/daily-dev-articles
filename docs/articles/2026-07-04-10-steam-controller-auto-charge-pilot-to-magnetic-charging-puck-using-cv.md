# Steam Controller Auto-Charge – pilot to magnetic charging puck using CV

- **Source:** Hacker News
- **Rank (today):** #10
- **Ranking metrics:** HN score 170
- **Published (UTC):** 2026-07-03 22:39
- **Original:** https://github.com/FossPrime/Steam-Controller-Auto-Charge

## Summary

Steam Controller Auto-Charge is an open-source web application designed to automatically pilot a Steam Controller into its magnetic charging puck using optical flow computer vision and WebHID telemetry. - Optical Flow Tracking: Utilizes OpenCV.js to track user-selected points on the controller and the charging puck via an overhead camera. - WebHID Telemetry & Haptic Navigation: Connects to the Triton Controller natively via WebHID, streaming input and telemetry (Report 67).

## Key Takeaways

- Navigates the controller towards the puck by firing 70Hz asymmetric haptic pulses through the internal dual Linear Resonant Actuators (LRAs).
- - Proximity Creep Mode: Automatically cuts haptic pulse frequency by 50% when the controller is within 150 pixels of the puck to ensure a gentle magnetic dock.
- - Battery Status Polling: Intercepts Report ID 121(0x79) to confirm successful magnetic charging, and parses Report ID67(0x43) to display live battery percentage and battery cell voltage (mV).

---
_Auto-generated daily digest entry._
