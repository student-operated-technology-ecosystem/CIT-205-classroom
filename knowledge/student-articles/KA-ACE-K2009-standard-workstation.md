# ACE Standard Workstation: Configuration and Validation Reference

**Status:** Student Draft (Version 0.2, Verified Draft), not approved operational guidance  
**Scenario:** During a support call, the team did not know what kind of workstation the user had, which led to unnecessary troubleshooting paths.  
**Applies to:** ACE classroom workstations (Dell Inspiron 5558 laptop, Windows 11 Pro). Values below were confirmed on one unit and are treated as the expected baseline until more units are checked.  
**Search terms:** standard workstation, baseline configuration, Dell Inspiron 5558, Windows 11 Pro, workstation validation, hardware specs, Wi-Fi, DHCP

## Problem and Symptoms

**Observed:** A technician began troubleshooting without knowing the user's computer type, operating system, or hardware. This created guesswork and wasted steps.

**Assumed:** That most ACE workstations share the same configuration. This is confirmed on one unit only.

This article gives any technician, including one who did not validate the machine personally, a reference to confirm whether a workstation matches the ACE standard before troubleshooting.

## Questions to Ask

- Is this an ACE classroom workstation, or a personal or non-standard device?
- What changed recently (new hardware, updates, moved to another room or network)?
- Is the laptop running on the charger or on battery only?
- Is the external monitor and mouse connected as usual?

## Before You Begin

- Get the user's permission before using their workstation.
- Standard user access is enough to view system information. Do not change settings that require administrator rights.
- Do not record usernames, passwords, or other personal information in tickets or notes.

## Expected Standard (Verified on One Unit)

| Item | Expected value | Status |
|---|---|---|
| Computer type | Dell Inspiron 5558 laptop | Verified |
| Operating system | Windows 11 Pro, version 24H2 | Verified |
| Processor | Intel Core i5-5200U @ 2.20 GHz | Verified |
| Installed RAM | 16.0 GB (DDR3) | Verified |
| Storage | 1 TB drive (Windows reports about 932 GB, which is normal) | Verified |
| Network | Wi-Fi, IPv4 address assigned automatically (DHCP) | Verified |
| Power | AC power via charger, battery present as backup | Observed on one unit, needs faculty review |
| Peripherals | External monitor and external mouse | Observed on one unit, needs faculty review |

## Troubleshooting Steps

1. **Check the computer model and hardware.** Open **Settings → System → About**. Compare the device name, processor, and installed RAM to the table above.
2. **Check the Windows version.** Press **Windows + R**, type `winver`, and press Enter. The expected result is Windows 11 Pro, version 24H2.
3. **Check storage.** Open **File Explorer → This PC**. A 1 TB drive shows as about 932 GB. This is expected, because Windows counts storage differently than the drive maker does.
4. **Check the network.** Open **Command Prompt** and run `ipconfig`. Confirm the Wi-Fi adapter has an IPv4 address, subnet mask, and default gateway.
   - If an address is present, the workstation is getting an address automatically. Do not treat any specific IP address as part of the standard, because the address can change.
   - If the address starts with `169.254`, the workstation did not receive an address from the network. Treat this as a network issue and follow the escalation steps below.
5. **Check power and peripherals.** Confirm the charger is connected and the external monitor and mouse work.
6. **Record any difference** between what you found and the expected standard before continuing.

## Likely Resolution

If the workstation matches the standard, the technician can rule out hardware or configuration differences and focus on the reported problem. If it does not match, the difference itself may explain the problem. Record it, and do not assume the article is wrong or the workstation is wrong until faculty confirms which one is correct.

## Verification

- Every item in the Expected Standard table was checked and recorded as a match or a difference.
- The technician knows the workstation type before starting deeper troubleshooting.
- The user confirms their original issue is resolved, or the ticket is escalated with the findings attached.

## Stop and Escalate

Stop and escalate to the instructor or the next support level when:

- the workstation does not match the standard and you do not know which is correct;
- a fix would require administrator rights, BIOS changes, or hardware changes;
- the workstation has no network address after the basic checks;
- private data, passwords, or personal files would need to be accessed.

In the handoff, include: what the user reported, which checks you performed, the values you found, and how they differ from this article.

## Sources and Related Knowledge

- ACE-NH-001 Workstation Validation (classroom validation record)
- ACE-NH-004A Knowledge Article Draft assignment
- CIT-205 Knowledge Article template

## Revision Notes

- Version 0.1 (09/08/2026): Initial candidate draft. Hardware and OS values listed, power and peripherals marked NEEDS VERIFICATION.
- Version 0.2: Revised after ACE-NH-001 validation. Added computer model (Dell Inspiron 5558) and OS version 24H2. Corrected network entry: the IP address differed from the draft, so the standard now says the address is assigned automatically instead of listing a fixed IP. Power and peripherals observed on one unit and flagged for faculty review. Specific network addresses removed for public posting.
