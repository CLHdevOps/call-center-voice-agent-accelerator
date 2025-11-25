# Discovery Questions - Phone System Assessment
## Azure Communication Services Migration Feasibility

**Client**: Mercy House & Sacred Grove
**Current Setup**: 17 phone lines across 4 locations

---

## Current Phone System

### Provider & Infrastructure

**1. Who is your current phone service provider?**
- [ ] Traditional carrier (AT&T, Verizon, etc.)
- [ ] VoIP provider (RingCentral, 8x8, etc.)
- [ ] On-premises PBX system
- [ ] Other: _______________

**2. What type of phone system do you have?**
- [ ] Traditional landlines (analog/POTS)
- [ ] PRI/T1 lines
- [ ] SIP trunking
- [ ] Hosted VoIP/cloud system
- [ ] Hybrid system
- [ ] Not sure

**3. How old is your current phone system?**
- [ ] Less than 2 years
- [ ] 2-5 years
- [ ] 5-10 years
- [ ] 10+ years
- [ ] Not sure

**4. Are you currently under contract with your phone provider?**
- [ ] Yes (expires: _______)
- [ ] No
- [ ] Month-to-month
- [ ] Not sure

---

## Phone Numbers & Lines

### Number Details

**5. Do you want to keep your existing phone numbers?**
- [ ] Yes, all of them (we'll port them to Azure)
- [ ] Some of them (specify which are critical)
- [ ] No, we can use new numbers
- [ ] Not sure

**6. List your phone numbers by location:**

**Location 1 (Mens Facility - Mercy House)**:
- Main intake line: _______________
- Additional lines: _______________
- Total lines: _____

**Location 2 (Womens Facility - Sacred Grove)**:
- Main intake line: _______________
- Additional lines: _______________
- Total lines: _____

**Location 3**: _______________
- Lines: _______________
- Total lines: _____

**Location 4**: _______________
- Lines: _______________
- Total lines: _____

**Total across all locations**: 17 lines

**7. Which numbers need to be ported vs. which can be replaced?**
- Critical numbers (must port): _______________
- Can be replaced: _______________

**8. Any toll-free numbers (800, 888, etc.)?**
- [ ] Yes: _______________
- [ ] No

---

## Usage Patterns

### Call Volume

**9. Approximate monthly call volume?**
- Incoming calls per month: _______________
- Outgoing calls per month: _______________
- Peak call times: _______________
- After-hours calls (estimated %): _______________

**10. Concurrent call capacity needed?**
- Maximum calls happening simultaneously: _____
- Average concurrent calls: _____

**11. International calling?**
- [ ] Yes, to which countries: _______________
- [ ] No
- [ ] Rarely

---

## Current Features in Use

### What You Use Today

**12. Which features do you actively use?** (check all that apply)
- [ ] Call forwarding
- [ ] Call transfer (attended/blind)
- [ ] Voicemail
- [ ] Voicemail-to-email
- [ ] Auto-attendant (press 1 for..., press 2 for...)
- [ ] Call recording
- [ ] Call queues (hold music, queue position)
- [ ] Hunt groups/ring groups
- [ ] Conference calling
- [ ] Extension dialing (dial 101 for John, etc.)
- [ ] Mobile app for staff
- [ ] Fax (analog or digital)
- [ ] Overhead paging/intercom
- [ ] Integration with other software: _______________

**13. Which features are CRITICAL (must have in new system)?**
- _______________
- _______________
- _______________

**14. Which features would be nice to have but aren't critical?**
- _______________
- _______________

---

## Staff & Devices

### User Setup

**15. How many staff members need phone access?**
- Total staff: _____
- Staff who answer intake calls: _____
- Staff who need extension/desk phone: _____
- Staff who need mobile access: _____

**16. What devices does staff currently use?**
- [ ] Desk phones (count: _____)
- [ ] Softphones (on computer)
- [ ] Mobile phones
- [ ] Mix of above

**17. Do you want to keep existing desk phones or move to softphones/apps?**
- [ ] Keep existing desk phones (we'll check compatibility)
- [ ] Move to computer-based softphones (headset + app)
- [ ] Move to mobile apps (use personal/company phones)
- [ ] Mix of options
- [ ] Not sure yet

**18. What's your internet connectivity like?**
- Internet provider: _______________
- Download speed: _____ Mbps
- Upload speed: _____ Mbps
- Backup internet connection?
  - [ ] Yes
  - [ ] No
- Any known internet reliability issues?
  - [ ] Yes (describe): _______________
  - [ ] No

---

## Special Requirements

### Compliance & Integration

**19. Do you have specific compliance requirements?**
- [ ] HIPAA (health information)
- [ ] Call recording retention policies
- [ ] E911 (emergency calling) requirements
- [ ] Other regulatory requirements: _______________

**20. Emergency calling (911)?**
- [ ] Must work from all locations
- [ ] Must work for remote staff
- [ ] Must include address/location info

**21. Do you need integration with any systems?**
- [ ] EHR/EMR system (name: _______________)
- [ ] CRM system (name: _______________)
- [ ] Microsoft Teams
- [ ] Other: _______________

**22. Faxing requirements?**
- [ ] No faxing needed
- [ ] Occasional faxing (can use eFax service)
- [ ] Heavy fax usage (need dedicated fax solution)
- [ ] Fax-to-email is acceptable

---

## Budget & Timeline

### Financial Considerations

**23. What are you currently paying per month for phone service?**
- Total monthly phone bill: $ _______________
- Per-line cost (if known): $ _______________
- Additional costs (long distance, features, maintenance): $ _______________

**24. What's your budget range for the new phone system?**
- [ ] Want to reduce current costs
- [ ] Willing to pay same as current
- [ ] Willing to invest more for better features
- [ ] Not sure / need recommendation

**25. Do you own or lease your current phone equipment?**
- [ ] Own (purchased outright)
- [ ] Lease (monthly payment)
- [ ] Mix
- [ ] Not sure

**26. Any hardware we need to account for replacing?**
- Physical phones: _____
- PBX/server equipment: _____
- Other equipment: _______________

---

## Migration Concerns

### Risk Assessment

**27. What are your biggest concerns about changing phone systems?**
- [ ] Downtime during migration
- [ ] Staff training/adoption
- [ ] Call quality issues
- [ ] Cost overruns
- [ ] Losing existing phone numbers
- [ ] Emergency calling reliability
- [ ] Internet dependency
- [ ] Other: _______________

**28. When would you ideally want to migrate?**
- [ ] ASAP (within 1-2 months)
- [ ] 3-6 months
- [ ] 6-12 months
- [ ] Wait until current contract expires: _____
- [ ] No specific timeline

**29. Can you have any downtime during migration, and if so, when?**
- [ ] After hours only (evenings/weekends)
- [ ] During specific hours: _______________
- [ ] Prefer zero downtime (we'll do phased migration)

**30. Who will be the primary point of contact for this project?**
- Name: _______________
- Role: _______________
- Email: _______________
- Phone: _______________
- Best time to reach: _______________

---

## Additional Notes

**31. Any other requirements, concerns, or questions?**

_______________________________________________________________________________

_______________________________________________________________________________

_______________________________________________________________________________

_______________________________________________________________________________

---

## ACS Migration Feasibility Assessment

**Based on answers above, we'll determine**:
- ✅ Can migrate to ACS? Yes/No
- ⚠️ Any blockers or special considerations?
- 💰 Estimated monthly cost
- 🗓️ Recommended timeline
- 🔧 Additional equipment/services needed

**Follow-up items after this meeting**:
1. Technical assessment of internet connectivity (if needed)
2. Desk phone compatibility check (if keeping existing phones)
3. Detailed cost comparison: current vs. ACS
4. Migration plan with specific dates/phases
5. Contract review (if under current provider contract)

---

## Quick Decision Matrix

**ACS is a GREAT fit if**:
- ✅ You have reliable high-speed internet
- ✅ Most features you need are standard (forwarding, voicemail, auto-attendant)
- ✅ You're willing to move to cloud-based system
- ✅ You want lower costs and more flexibility

**ACS may require additional planning if**:
- ⚠️ Heavy fax usage (need alternative fax solution)
- ⚠️ Specialized hardware integrations (overhead paging, door phones)
- ⚠️ Very limited or unreliable internet
- ⚠️ Locked into long-term contract with current provider

**ACS is likely NOT a fit if**:
- ❌ No internet connectivity or very poor internet
- ❌ Regulatory requirements prevent cloud telephony
- ❌ Organization policy prohibits cloud services

---

**Next Step**: Based on these answers, we'll provide a detailed ACS migration proposal with exact pricing and timeline.
