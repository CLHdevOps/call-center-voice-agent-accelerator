# Pricing Proposal - Mercy House & Sacred Grove
## AI Voice Receptionist + Azure Communication Services

**Date**: [Insert Date]
**Valid Through**: 30 days from date above

---

## PHASE 1: AI Voice Receptionist (Grace)

### One-Time Setup & Development

| Item | Description | Price |
|------|-------------|-------|
| **Initial Setup & Configuration** | Azure infrastructure setup, Voice Live API configuration, security setup | **$2,500** |
| **AI Training & Customization** | Custom prompt development for Mercy House/Sacred Grove, voice selection, conversation flow optimization | **$3,000** |
| **Integration Development** | WebSocket handlers, conversation logging, ACS phone integration | **$2,000** |
| **Testing & QA** | Comprehensive testing with various caller scenarios, quality assurance | **$1,500** |
| **Staff Training** | Training sessions for intake coordinators, documentation, admin portal walkthrough | **$1,000** |
| **TOTAL ONE-TIME** | | **$10,000** |

### Monthly Recurring Costs

| Item | Description | Monthly Price |
|------|-------------|---------------|
| **Azure Infrastructure** | Container Apps hosting, AI Services, logging/monitoring | **$150** |
| **Azure Voice Live API** | Real-time voice conversation AI (estimated 500 minutes/month @ $0.15/min) | **$75** |
| **Conversation Logging Storage** | Secure storage for conversation logs and analysis | **$25** |
| **Support & Maintenance** | Bug fixes, prompt refinements, monthly performance review | **$500** |
| **Monitoring & Quality Assurance** | Conversation quality monitoring, timing analysis, optimization recommendations | **$250** |
| **TOTAL MONTHLY** | | **$1,000** |

**Notes**:
- Voice API charges based on actual usage (above is estimate for ~500 minutes/month)
- First 3 months includes extra support for optimization
- Annual pre-pay discount: 10% off monthly fees ($10,800 instead of $12,000)

---

## PHASE 2: Azure Communication Services (Phone System)

### One-Time Migration Costs

| Item | Description | Price |
|------|-------------|-------|
| **System Design & Planning** | Network assessment, migration plan, call flow design | **$2,500** |
| **Number Porting** | Port existing phone numbers to Azure (up to 20 numbers) | **$500** |
| **ACS Configuration** | Call routing, auto-attendant setup, voicemail config, emergency calling | **$3,000** |
| **Integration with AI Receptionist** | Connect Grace AI to phone system, call routing logic | **$2,000** |
| **Testing & Migration** | Phased migration, testing, cutover support | **$2,000** |
| **Staff Training** | Training on new phone system, apps, features | **$1,000** |
| **TOTAL ONE-TIME** | | **$11,000** |

### Monthly Recurring Costs (17 Lines)

| Item | Calculation | Monthly Price |
|------|-------------|---------------|
| **Phone Numbers** | 17 numbers × $2/number | **$34** |
| **Inbound Calling** | 2,000 minutes × $0.013/min | **$26** |
| **Outbound Calling** | 1,000 minutes × $0.013/min | **$13** |
| **SMS (optional)** | 500 messages × $0.0075/message | **$4** |
| **Call Recording Storage** | 50 GB × $0.05/GB | **$3** |
| **Management & Support** | System admin, monitoring, troubleshooting | **$400** |
| **TOTAL MONTHLY** | | **$480** |

**Pricing Notes**:
- Above assumes moderate usage (2,000 inbound / 1,000 outbound minutes per month)
- Actual usage billed based on consumption
- International calling: Additional per-minute charges (varies by country)
- Toll-free numbers: $2/month + $0.022/minute inbound

**Cost Comparison Example**:
- **Traditional phone system**: Often $40-60/line = $680-1,020/month for 17 lines
- **Our ACS solution**: $480/month (17 lines + support)
- **Estimated savings**: $200-540/month or $2,400-6,480/year

---

## PHASE 3: EHR Integration (Optional)

### Custom Integration Development

**Pricing depends on EHR system and complexity**. Below are typical scenarios:

#### Scenario A: EHR with Modern REST API

| Item | Description | Price |
|------|-------------|-------|
| **API Integration Development** | Connect Grace to EHR API, data mapping, authentication | **$8,000** |
| **Intake Workflow Automation** | Auto-create intake records, assign to coordinators, notifications | **$4,000** |
| **Testing & Deployment** | Integration testing, UAT, production deployment | **$2,000** |
| **Documentation & Training** | Staff training on integrated workflow | **$1,000** |
| **TOTAL ONE-TIME** | | **$15,000** |
| **Monthly Support** | Ongoing integration maintenance, API monitoring | **$300** |

#### Scenario B: EHR with Limited/Legacy API

| Item | Description | Price |
|------|-------------|-------|
| **Custom Integration Layer** | Build middleware for data exchange, field mapping | **$12,000** |
| **Workflow Development** | Automated intake creation, task assignment | **$5,000** |
| **Testing & Deployment** | Comprehensive testing, deployment | **$3,000** |
| **TOTAL ONE-TIME** | | **$20,000** |
| **Monthly Support** | Integration monitoring, maintenance, updates | **$500** |

#### Scenario C: No API Available (Alternative Approach)

| Item | Description | Price |
|------|-------------|-------|
| **Email-to-EHR Workflow** | Formatted email sent to intake coordinators with caller data | **$3,000** |
| **Spreadsheet Export** | Daily export of intake data to Excel/CSV for manual entry | **$2,000** |
| **TOTAL ONE-TIME** | | **$5,000** |
| **Monthly Support** | Monitoring and support | **$150** |

**Common EHR Systems & Estimated Integration Complexity**:
- ✅ **Low Complexity** ($8-10k): Epic (with API access), Cerner, athenahealth, Allscripts
- ⚠️ **Medium Complexity** ($12-15k): Older EMR systems, limited APIs, custom systems
- ⚠️ **High Complexity** ($20-25k): Legacy systems, no API, requires custom middleware

---

## Additional Optional Features

### À La Carte Enhancements

| Feature | Description | One-Time | Monthly |
|---------|-------------|----------|---------|
| **SMS Auto-Response** | Auto-reply to text messages with intake info | $2,000 | $100 |
| **Bilingual Spanish Support** | Fully bilingual English/Spanish AI receptionist | $3,000 | $150 |
| **After-Hours Emergency Escalation** | Forward critical cases to on-call staff | $2,500 | $100 |
| **CRM Integration** | Integrate with Salesforce, HubSpot, etc. | $5,000 | $200 |
| **Custom Reporting Dashboard** | Real-time dashboards for call volume, conversion rates | $4,000 | $200 |
| **Microsoft Teams Integration** | Take calls directly in Teams app | $3,000 | $150 |
| **Additional AI Assistants** | Specialized AI for different departments | $5,000 ea | $500 ea |

---

## Package Pricing (Bundled Discounts)

### Package 1: AI Receptionist Only
**Best for**: Testing AI capability before phone system migration

| Component | Price |
|-----------|-------|
| Setup (Phase 1) | $10,000 |
| Monthly (Phase 1) | $1,000/month |
| **12-Month Total** | **$22,000** |

### Package 2: AI Receptionist + Phone System
**Best for**: Complete communication system modernization

| Component | Price |
|-----------|-------|
| Setup (Phase 1 + 2) | $19,000 (save $2,000) |
| Monthly (Phase 1 + 2) | $1,400/month (save $80/month) |
| **12-Month Total** | **$35,800** |

### Package 3: Complete Solution (Phases 1 + 2 + 3)
**Best for**: Fully automated intake workflow

| Component | Price |
|-----------|-------|
| Setup (All Phases) | $32,000 (save $4,000) |
| Monthly (All Phases) | $1,650/month (save $150/month) |
| **12-Month Total** | **$51,800** |

**Pre-Payment Discounts**:
- Pay 6 months up front: 5% discount
- Pay 12 months up front: 10% discount

---

## Payment Terms

### Standard Terms

- **Setup Fees**: 50% deposit at contract signing, 50% at go-live
- **Monthly Fees**: Billed monthly in advance, due net 15
- **Azure Consumption**: Actual usage billed monthly (Voice API minutes, call minutes)

### Alternative Payment Options

**Option 1: Monthly Payment Plan**
- Spread setup costs over 12 months
- Example: $10,000 setup becomes $900/month for 12 months (includes $800 setup + standard $1,000 monthly)

**Option 2: Annual Pre-Pay**
- Pay full year up front for 10% discount
- Example: Package 1 becomes $19,800 (instead of $22,000)

---

## ROI Analysis

### Cost Savings - Phone System Migration

**Current Traditional Phone System (estimated)**:
- 17 lines @ $50/line/month = $850/month
- Equipment maintenance = $100/month
- Long distance charges = $50/month
- **Total Current: $1,000/month = $12,000/year**

**New Azure Communication Services**:
- 17 lines + support = $480/month = $5,760/year
- **Annual Savings: $6,240**

**Payback Period on ACS Migration**:
- Setup cost: $11,000
- Monthly savings: $520
- **Payback: 21 months (less than 2 years)**

### Staff Time Savings - AI Receptionist

**Current State** (estimated):
- Intake calls per week: 40 calls
- Average call duration: 10 minutes
- Staff time per week: 400 minutes = **6.7 hours**
- Staff hourly rate: $25/hour
- **Weekly cost: $167.50 = $8,700/year**

**With Grace AI**:
- Grace handles 60% of initial intake calls completely
- Staff only calls back qualified leads
- Staff time saved: 4 hours/week = **$5,200/year**

**Combined Annual Savings**:
- Phone system: $6,240
- Staff time: $5,200
- **Total: $11,440/year**

**Total First-Year Cost** (Package 2):
- Setup + 12 months: $35,800
- Annual savings: $11,440
- **Net first-year cost: $24,360**

**Year 2 and Beyond**:
- Annual cost: $16,800
- Annual savings: $11,440
- **Net annual cost: $5,360**

---

## What's NOT Included

**Client Responsibilities**:
- High-speed internet connection (minimum 10 Mbps upload per location)
- Internal IT support for workstation/computer issues
- Staff headsets (if using softphones) - estimated $50-100 per user
- Mobile devices (if using mobile app for calls)
- Content for FAQ/knowledge base about specific programs

**Additional Costs May Apply For**:
- Custom hardware integrations (door phones, paging systems)
- Third-party software licenses (if needed for integrations)
- International calling (per-minute charges vary by country)
- Toll-free numbers (higher per-minute rates)
- Significant scope changes during implementation

---

## Next Steps & Timeline

### If You Proceed Today

**Week 1-2**: Contract & Kickoff
- Sign agreement
- 50% deposit payment
- Kickoff meeting with technical team
- Finalize requirements

**Week 3-4**: Development & Configuration
- Azure infrastructure setup
- Grace AI training and customization
- (If applicable) ACS phone system configuration

**Week 5**: Testing & Training
- Internal testing with your team
- Staff training sessions
- Refinements based on feedback

**Week 6**: Go-Live
- Deploy to production
- Final payment (remaining 50%)
- Initial monitoring and optimization

**Month 2-3**: Optimization
- Review conversation logs
- Refine prompts based on real calls
- Ongoing quality improvements

---

## Guarantee & Service Level Agreement

**Our Commitments**:
- **99.9% uptime** for AI receptionist service
- **99.95% uptime** for ACS phone service (Azure SLA)
- Response to critical issues within 2 hours
- Monthly performance reviews included
- 30-day money-back guarantee on setup fees if system doesn't meet agreed specifications

**Your Protection**:
- No long-term contracts required (month-to-month after first year)
- Can cancel with 30 days notice
- Own your conversation data (exportable at any time)
- Number portability (can move phone numbers to another provider if needed)

---

## Questions?

**Contact Information**:
[Your Name]
[Your Title]
[Your Company]
[Email]
[Phone]

**Schedule a Follow-Up**:
- Technical deep-dive demo
- Reference calls with current clients
- Review of sample conversation logs
- Detailed integration planning session

---

## Approval & Signature

**Authorized by**:

Client Name: ___________________________________

Title: ___________________________________

Signature: ___________________________________ Date: __________

---

**Preferred Package**:
- [ ] Package 1: AI Receptionist Only ($22,000 first year)
- [ ] Package 2: AI + Phone System ($35,800 first year)
- [ ] Package 3: Complete Solution ($51,800 first year)
- [ ] Custom: ___________________________________

**Payment Method**:
- [ ] Standard terms (50% deposit, 50% at go-live, monthly billing)
- [ ] Monthly payment plan (spread setup over 12 months)
- [ ] Annual pre-pay (10% discount)

**Add-Ons**:
- [ ] SMS Auto-Response
- [ ] Bilingual Spanish Support
- [ ] After-Hours Emergency Escalation
- [ ] Custom Reporting Dashboard
- [ ] Other: ___________________________________
