# A Matter Wi-Fi Light Bulb in Rust on the Raspberry Pi Pico 2 W

- **Source:** Hacker News
- **Rank (today):** #9
- **Ranking metrics:** HN score 156
- **Published (UTC):** 2026-06-08 00:17
- **Original:** https://github.com/melastmohican/rust-rpico2-embassy-examples

## Summary

This repository contains examples for the Raspberry Pi Pico 2 (RP2350) board, written in Rust using the Embassy async framework. cargo generate --git https://github.com/ImplFerris/pico2-template.git --name rust-rpico2-embassy-examplesBoard: Raspberry Pi Pico 2 - MCU: RP2350 (Dual-core Arm Cortex-M33 and RISC-V cores) - On-board peripherals: - LED on GPIO25 - I2C pins: - I2C0 SDA: GPIO4 - I2C0 SCL: GPIO5 - I2C1 SDA: GPIO2 - I2C1 SCL: GPIO3 - UART pins: - UART0 TX: GPIO0, UART0 RX: GPIO1 - UART1 TX: GPIO8, UART1 RX: GPIO9 Reads temperature and humidity from an HS3003 sensor using the Embassy async framework. cargo run --example hs3003_i2cWiring (Arduino Modulino Thermo): Modulino -> RPi Pico 2 ---------- -------------- GND (black) -> GND VCC (red) -> 3.3V SCL (yellow)-> GPIO5 (Pin 7) (I2C0 SCL) SDA (blue) -> GPIO4 (Pin 6) (I2C0 SDA) About HS3003: The Renesas HS3003 is a high-performance temperature and humidity sensor: - Temperature range: -40°C to +125°C (±0.2°C accuracy) - Humidity range: 0% to 100% RH (±1.5% accuracy) - 14-bit resolution for both measurements - Ultra-low power consumption Reads accelerometer data from an ADXL345 sensor over I2C0 using Embassy.

## Key Takeaways

- cargo run --example adxl345_i2cWiring: ADXL345 -> RPi Pico 2 ---------- -------------- GND (black) -> GND VCC (red) -> 3.3V SCL (yellow)-> GPIO5 (Pin 7) (I2C0 SCL) SDA (blue) -> GPIO4 (Pin 6) (I2C0 SDA) About ADXL345: The ADXL345 is a small, thin, low power, 3-axis accelerometer with high resolution (13-bit) measurement at up to ±16 g.
- Digital output data is formatted as 16-bit twos complement and is accessible through either an SPI (3- or 4-wire) or I2C digital interface.
- Displays a 320x240 image of Zermatt on the Adafruit 2.2" TFT LCD display in landscape mode.

---
_Auto-generated daily digest entry._
