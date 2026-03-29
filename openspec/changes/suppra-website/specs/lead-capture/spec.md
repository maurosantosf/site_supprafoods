## ADDED Requirements

### Requirement: Segmented Contact Forms
The system SHALL provide dedicated contact forms that segment users based on their intent (e.g., "Quero ser um parceiro logístico", "Quero revender produtos", "Fornecedores").

#### Scenario: User submits a business inquiry
- **WHEN** a user clicks on "Contato" or a specific "Fale com um Consultor" button
- **THEN** they are presented with a form that uniquely identifies their business need

### Requirement: Lead Routing
The system SHALL ensure that submitted forms capture essential B2B data (Company Name, CNPJ, Contact Person, Phone) and route the information to the correct commercial email.

#### Scenario: Commercial team receives a lead
- **WHEN** a retailer submits a form requesting a quote
- **THEN** an email notification is sent to the sales team with all the captured B2B information formatted clearly
