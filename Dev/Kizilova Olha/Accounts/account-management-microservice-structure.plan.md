<!-- 4b36a91c-5619-4c94-bf4b-910119ef7862 59d338e0-163b-43be-bec5-94b0d0d3bfaa -->
# Структура микросервиса управления аккаунтами (Node.js + PostgreSQL)

## 1. Структура базы данных PostgreSQL

### 1.1 Таблица accounts

Аккаунты сервисов (Gmail, LinkedIn, телефон, GitHub и т.д.):

```sql
CREATE TABLE accounts (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    tool_id INTEGER NOT NULL, -- ссылка на другой микросервис (tools)
    login VARCHAR(255) NOT NULL,
    password TEXT, -- зашифрован, опционально
    can_verify_others BOOLEAN DEFAULT false,
    status_id INTEGER NOT NULL, -- ссылка на другой микросервис (statuses)
    owner_id INTEGER NOT NULL,
    metadata JSONB DEFAULT '{}',
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_used_at TIMESTAMP,
    usage_count INTEGER DEFAULT 0
);

CREATE INDEX idx_accounts_tool_id ON accounts(tool_id);
CREATE INDEX idx_accounts_status_id ON accounts(status_id);
CREATE INDEX idx_accounts_owner_id ON accounts(owner_id);
CREATE INDEX idx_accounts_can_verify_others ON accounts(can_verify_others);
CREATE INDEX idx_accounts_last_used_at ON accounts(last_used_at);
CREATE INDEX idx_accounts_created_at ON accounts(created_at);
```

### 1.2 Таблица job_accounts

Аккаунты на сайтах вакансий:

```sql
CREATE TABLE job_accounts (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    job_site_id INTEGER NOT NULL, -- ссылка на другой микросервис (job_sites)
    login VARCHAR(255) NOT NULL,
    password TEXT NOT NULL, -- зашифрован
    profile_link TEXT,
    status_id INTEGER NOT NULL, -- ссылка на другой микросервис (statuses)
    owner_id INTEGER NOT NULL,
    available_job_posts INTEGER DEFAULT 0,
    active_job_posts INTEGER DEFAULT 0,
    metadata JSONB DEFAULT '{}',
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_used_at TIMESTAMP,
    usage_count INTEGER DEFAULT 0
);

CREATE INDEX idx_job_accounts_job_site_id ON job_accounts(job_site_id);
CREATE INDEX idx_job_accounts_status_id ON job_accounts(status_id);
CREATE INDEX idx_job_accounts_owner_id ON job_accounts(owner_id);
CREATE INDEX idx_job_accounts_last_used_at ON job_accounts(last_used_at);
CREATE INDEX idx_job_accounts_created_at ON job_accounts(created_at);
```

### 1.3 Таблица account_verifications

Связь Account аккаунтов с Account аккаунтами для верификации:

```sql
CREATE TABLE account_verifications (
    id SERIAL PRIMARY KEY,
    account_id INTEGER NOT NULL REFERENCES accounts(id) ON DELETE CASCADE,
    verification_account_id INTEGER NOT NULL REFERENCES accounts(id) ON DELETE CASCADE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(account_id, verification_account_id)
);

CREATE INDEX idx_account_verifications_account_id ON account_verifications(account_id);
CREATE INDEX idx_account_verifications_verification_account_id ON account_verifications(verification_account_id);
```

### 1.4 Таблица account_verification_subscriptions

Подписки на верификацию аккаунтов с историей:

```sql
CREATE TABLE account_verification_subscriptions (
    id SERIAL PRIMARY KEY,
    account_verification_id INTEGER NOT NULL REFERENCES account_verifications(id) ON DELETE CASCADE,
    plan_id INTEGER, -- ссылка на микросервис с планами подписки (опционально)
    plan_name VARCHAR(255), -- название плана (если нет отдельного микросервиса)
    status VARCHAR(50) NOT NULL DEFAULT 'active', -- active, expired, cancelled, suspended
    started_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    expires_at TIMESTAMP, -- когда заканчивается подписка
    cancelled_at TIMESTAMP, -- когда была отменена
    auto_renew BOOLEAN DEFAULT false, -- автопродление
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_verification_subscriptions_account_verification_id ON account_verification_subscriptions(account_verification_id);
CREATE INDEX idx_verification_subscriptions_status ON account_verification_subscriptions(status);
CREATE INDEX idx_verification_subscriptions_expires_at ON account_verification_subscriptions(expires_at);
CREATE INDEX idx_verification_subscriptions_started_at ON account_verification_subscriptions(started_at);
```

### 1.5 Таблица verification_subscription_payments

История платежей за подписки на верификацию:

```sql
CREATE TABLE verification_subscription_payments (
    id SERIAL PRIMARY KEY,
    subscription_id INTEGER NOT NULL REFERENCES account_verification_subscriptions(id) ON DELETE CASCADE,
    amount DECIMAL(10, 2) NOT NULL,
    currency VARCHAR(3) DEFAULT 'USD',
    payment_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    payment_method VARCHAR(50), -- card, bank_transfer, etc.
    payment_status VARCHAR(50) NOT NULL DEFAULT 'pending', -- pending, completed, failed, refunded
    transaction_id VARCHAR(255), -- ID транзакции из платежной системы
    invoice_number VARCHAR(255),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_subscription_payments_subscription_id ON verification_subscription_payments(subscription_id);
CREATE INDEX idx_subscription_payments_payment_date ON verification_subscription_payments(payment_date);
CREATE INDEX idx_subscription_payments_payment_status ON verification_subscription_payments(payment_status);
```

### 1.6 Таблица job_account_verifications

Связь JobAccount аккаунтов с Account аккаунтами для верификации:

```sql
CREATE TABLE job_account_verifications (
    id SERIAL PRIMARY KEY,
    job_account_id INTEGER NOT NULL REFERENCES job_accounts(id) ON DELETE CASCADE,
    verification_account_id INTEGER NOT NULL REFERENCES accounts(id) ON DELETE CASCADE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(job_account_id, verification_account_id)
);

CREATE INDEX idx_job_account_verifications_job_account_id ON job_account_verifications(job_account_id);
CREATE INDEX idx_job_account_verifications_verification_account_id ON job_account_verifications(verification_account_id);
```

## 2. Модели данных (TypeScript)

### 2.1 Модель Account

```typescript
interface Account {
    id: number;
    name: string;
    tool_id: number; // ссылка на микросервис tools
    login: string;
    password: string | null; // зашифрован, опционально
    can_verify_others: boolean;
    status_id: number; // ссылка на микросервис statuses
    owner_id: number;
    metadata: Record<string, any>;
    notes: string | null;
    created_at: Date;
    updated_at: Date;
    last_used_at: Date | null;
    usage_count: number;
}

interface AccountWithVerifications extends Account {
    verification_accounts?: Account[]; // через JOIN с account_verifications
    verified_by_accounts?: Account[]; // через обратный JOIN
    verified_by_job_accounts?: JobAccount[]; // через обратный JOIN с job_account_verifications
}
```

### 2.2 Модель JobAccount

```typescript
interface JobAccount {
    id: number;
    name: string;
    job_site_id: number; // ссылка на микросервис job_sites
    login: string;
    password: string;
    profile_link: string | null;
    status_id: number; // ссылка на микросервис statuses
    owner_id: number;
    available_job_posts: number;
    active_job_posts: number;
    metadata: Record<string, any>;
    notes: string | null;
    created_at: Date;
    updated_at: Date;
    last_used_at: Date | null;
    usage_count: number;
}

interface JobAccountWithVerifications extends JobAccount {
    verification_accounts?: Account[]; // через JOIN с job_account_verifications
}
```

### 2.3 Модели связей

```typescript
interface AccountVerification {
    id: number;
    account_id: number;
    verification_account_id: number;
    created_at: Date;
}

interface JobAccountVerification {
    id: number;
    job_account_id: number;
    verification_account_id: number;
    created_at: Date;
}
```

### 2.4 Модели подписок

```typescript
interface AccountVerificationSubscription {
    id: number;
    account_verification_id: number;
    plan_id: number | null;
    plan_name: string | null;
    status: 'active' | 'expired' | 'cancelled' | 'suspended';
    started_at: Date;
    expires_at: Date | null;
    cancelled_at: Date | null;
    auto_renew: boolean;
    created_at: Date;
    updated_at: Date;
}

interface AccountVerificationSubscriptionWithPayments extends AccountVerificationSubscription {
    payments?: VerificationSubscriptionPayment[];
}

interface VerificationSubscriptionPayment {
    id: number;
    subscription_id: number;
    amount: number;
    currency: string;
    payment_date: Date;
    payment_method: string | null;
    payment_status: 'pending' | 'completed' | 'failed' | 'refunded';
    transaction_id: string | null;
    invoice_number: string | null;
    notes: string | null;
    created_at: Date;
}
```

## 3. Структура проекта Node.js

```
account-service/
├── src/
│   ├── config/
│   │   ├── database.ts          # PostgreSQL connection
│   │   └── env.ts                # Environment variables
│   ├── models/
│   │   ├── Account.ts            # Account model
│   │   ├── JobAccount.ts         # JobAccount model
│   │   ├── AccountVerification.ts
│   │   └── JobAccountVerification.ts
│   ├── repositories/
│   │   ├── AccountRepository.ts
│   │   ├── JobAccountRepository.ts
│   │   └── VerificationRepository.ts
│   ├── services/
│   │   ├── AccountService.ts
│   │   ├── JobAccountService.ts
│   │   └── VerificationService.ts
│   ├── controllers/
│   │   ├── AccountController.ts
│   │   ├── JobAccountController.ts
│   │   └── VerificationController.ts
│   ├── routes/
│   │   ├── accounts.routes.ts
│   │   ├── jobAccounts.routes.ts
│   │   └── verifications.routes.ts
│   ├── middleware/
│   │   ├── auth.ts
│   │   ├── validation.ts
│   │   └── errorHandler.ts
│   ├── utils/
│   │   ├── encryption.ts
│   │   ├── queryBuilder.ts
│   │   └── logger.ts
│   ├── migrations/
│   │   ├── 001_create_accounts.sql
│   │   ├── 002_create_job_accounts.sql
│   │   ├── 003_create_account_verifications.sql
│   │   └── 004_create_job_account_verifications.sql
│   ├── app.ts                    # Express app
│   └── server.ts                 # Server entry point
├── package.json
├── tsconfig.json
├── .env.example
└── README.md
```

## 4. Примеры запросов

### 4.1 Получить Account с верификационными аккаунтами

```sql
SELECT 
    a.*,
    json_agg(DISTINCT jsonb_build_object(
        'id', av_account.id,
        'name', av_account.name,
        'tool_id', av_account.tool_id
    )) FILTER (WHERE av_account.id IS NOT NULL) as verification_accounts,
    json_agg(DISTINCT jsonb_build_object(
        'id', verified_account.id,
        'name', verified_account.name,
        'tool_id', verified_account.tool_id
    )) FILTER (WHERE verified_account.id IS NOT NULL) as verified_by_accounts
FROM accounts a
LEFT JOIN account_verifications av ON a.id = av.account_id
LEFT JOIN accounts av_account ON av.verification_account_id = av_account.id
LEFT JOIN account_verifications av_reverse ON a.id = av_reverse.verification_account_id
LEFT JOIN accounts verified_account ON av_reverse.account_id = verified_account.id
WHERE a.id = $1
GROUP BY a.id;
```

### 4.2 Получить JobAccount с верификационными аккаунтами

```sql
SELECT 
    ja.*,
    json_agg(DISTINCT jsonb_build_object(
        'id', a.id,
        'name', a.name,
        'tool_id', a.tool_id
    )) FILTER (WHERE a.id IS NOT NULL) as verification_accounts
FROM job_accounts ja
LEFT JOIN job_account_verifications jav ON ja.id = jav.job_account_id
LEFT JOIN accounts a ON jav.verification_account_id = a.id
WHERE ja.id = $1
GROUP BY ja.id;
```

### 4.3 Получить Account с количеством верифицируемых аккаунтов

```sql
SELECT 
    a.*,
    COUNT(DISTINCT av.account_id) as verified_accounts_count,
    COUNT(DISTINCT jav.job_account_id) as verified_job_accounts_count
FROM accounts a
LEFT JOIN account_verifications av ON a.id = av.verification_account_id
LEFT JOIN job_account_verifications jav ON a.id = jav.verification_account_id
WHERE a.can_verify_others = true
GROUP BY a.id;
```

### 4.4 Получить Account Verification с активной подпиской и платежами

```sql
SELECT 
    av.*,
    json_agg(DISTINCT jsonb_build_object(
        'id', avs.id,
        'plan_name', avs.plan_name,
        'status', avs.status,
        'started_at', avs.started_at,
        'expires_at', avs.expires_at,
        'auto_renew', avs.auto_renew,
        'payments', (
            SELECT json_agg(jsonb_build_object(
                'id', vsp.id,
                'amount', vsp.amount,
                'currency', vsp.currency,
                'payment_date', vsp.payment_date,
                'payment_status', vsp.payment_status
            ))
            FROM verification_subscription_payments vsp
            WHERE vsp.subscription_id = avs.id
        )
    )) FILTER (WHERE avs.id IS NOT NULL) as subscriptions
FROM account_verifications av
LEFT JOIN account_verification_subscriptions avs ON av.id = avs.account_verification_id
WHERE av.id = $1
GROUP BY av.id;
```

### 4.5 Получить все активные подписки, которые скоро истекают

```sql
SELECT 
    avs.*,
    av.account_id,
    av.verification_account_id,
    a.name as account_name,
    va.name as verification_account_name
FROM account_verification_subscriptions avs
JOIN account_verifications av ON avs.account_verification_id = av.id
JOIN accounts a ON av.account_id = a.id
JOIN accounts va ON av.verification_account_id = va.id
WHERE avs.status = 'active'
  AND avs.expires_at IS NOT NULL
  AND avs.expires_at BETWEEN CURRENT_TIMESTAMP AND CURRENT_TIMESTAMP + INTERVAL '7 days'
ORDER BY avs.expires_at ASC;
```

### 4.6 Получить историю платежей за подписку

```sql
SELECT 
    vsp.*,
    avs.plan_name,
    avs.status as subscription_status
FROM verification_subscription_payments vsp
JOIN account_verification_subscriptions avs ON vsp.subscription_id = avs.id
WHERE vsp.subscription_id = $1
ORDER BY vsp.payment_date DESC;
```

### 4.7 Получить статистику по подпискам для Account Verification

```sql
SELECT 
    av.id,
    COUNT(DISTINCT avs.id) as total_subscriptions,
    COUNT(DISTINCT CASE WHEN avs.status = 'active' THEN avs.id END) as active_subscriptions,
    COUNT(DISTINCT CASE WHEN avs.status = 'expired' THEN avs.id END) as expired_subscriptions,
    SUM(CASE WHEN vsp.payment_status = 'completed' THEN vsp.amount ELSE 0 END) as total_paid_amount,
    MAX(vsp.payment_date) as last_payment_date
FROM account_verifications av
LEFT JOIN account_verification_subscriptions avs ON av.id = avs.account_verification_id
LEFT JOIN verification_subscription_payments vsp ON avs.id = vsp.subscription_id
WHERE av.id = $1
GROUP BY av.id;
```

## 5. API Endpoints

### 5.1 Accounts

- `GET /api/accounts` - список аккаунтов с фильтрацией
- `GET /api/accounts/:id` - детали аккаунта с верификационными связями
- `POST /api/accounts` - создание аккаунта
- `PUT /api/accounts/:id` - обновление аккаунта
- `DELETE /api/accounts/:id` - удаление аккаунта
- `GET /api/accounts/:id/verified-accounts` - список Account аккаунтов, верифицируемых через этот аккаунт
- `GET /api/accounts/:id/verified-job-accounts` - список JobAccount аккаунтов, верифицируемых через этот аккаунт

### 5.2 Job Accounts

- `GET /api/job-accounts` - список аккаунтов вакансий с фильтрацией
- `GET /api/job-accounts/:id` - детали аккаунта с верификационными связями
- `POST /api/job-accounts` - создание JobAccount аккаунта
- `PUT /api/job-accounts/:id` - обновление JobAccount аккаунта
- `DELETE /api/job-accounts/:id` - удаление JobAccount аккаунта

### 5.3 Verifications

- `GET /api/accounts?can_verify_others=true` - список Account аккаунтов, которые могут использоваться для верификации
- `GET /api/accounts?can_verify_others=true&tool_id=2` - аккаунты определенного типа для верификации
- `POST /api/accounts/:id/verifications` - добавить Account аккаунт для верификации
- `POST /api/job-accounts/:id/verifications` - добавить Account аккаунт для верификации JobAccount
- `DELETE /api/accounts/:id/verifications/:verification_account_id` - отвязать Account аккаунт верификации
- `DELETE /api/job-accounts/:id/verifications/:verification_account_id` - отвязать Account аккаунт верификации от JobAccount

### 5.4 Subscriptions

- `GET /api/account-verifications/:id/subscriptions` - список подписок для верификации
- `GET /api/account-verifications/:id/subscriptions/active` - активные подписки
- `POST /api/account-verifications/:id/subscriptions` - создать подписку на верификацию
- `PUT /api/subscriptions/:id` - обновить подписку
- `DELETE /api/subscriptions/:id` - отменить подписку
- `GET /api/subscriptions/expiring-soon` - подписки, которые скоро истекают
- `GET /api/subscriptions/:id` - детали подписки с платежами
- `GET /api/subscriptions/:id/statistics` - статистика по подписке

### 5.5 Payments

- `GET /api/subscriptions/:id/payments` - история платежей за подписку
- `POST /api/subscriptions/:id/payments` - добавить платеж
- `PUT /api/payments/:id` - обновить статус платежа
- `GET /api/payments/:id` - детали платежа

### 5.6 Filters

- `GET /api/accounts?tool_id=2&status_id=1`
- `GET /api/accounts?owner_id=2&tool_id=1`
- `GET /api/accounts?verification_accounts[]=1` - Account аккаунты, верифицируемые через указанный аккаунт
- `GET /api/job-accounts?job_site_id=1&status_id=1`
- `GET /api/job-accounts?verification_accounts[]=1` - JobAccount аккаунты, верифицируемые через указанный Account

## 6. Миграция данных

### 6.1 Скрипт миграции из существующих файлов

- Чтение `Job_Account_prod.json` → преобразование в структуру job_accounts
- Чтение `Account_prod.md` (JSON внутри) → преобразование в структуру accounts
- Чтение кластеров `LeadAccount_JSON_Clusters` → объединение и преобразование в accounts
- Создание телефонных аккаунтов из номеров телефонов в metadata как отдельные accounts с соответствующим tool_id
- Создание связей в таблице account_verifications
- Создание связей в таблице job_account_verifications
- Определение accounts, которые могут верифицировать другие (can_verify_others = true для Gmail и phone)

## 7. Зависимости (package.json)

```json
{
  "dependencies": {
    "express": "^4.18.2",
    "pg": "^8.11.0",
    "dotenv": "^16.3.1",
    "bcrypt": "^5.1.1",
    "jsonwebtoken": "^9.0.2",
    "zod": "^3.22.4",
    "winston": "^3.10.0"
  },
  "devDependencies": {
    "@types/express": "^4.17.17",
    "@types/node": "^20.5.0",
    "@types/pg": "^8.10.2",
    "@types/bcrypt": "^5.0.0",
    "@types/jsonwebtoken": "^9.0.2",
    "typescript": "^5.1.6",
    "ts-node": "^10.9.1",
    "nodemon": "^3.0.1"
  }
}
```

### To-dos

- [ ] Создать детальную JSON структуру для всех типов аккаунтов (Account, VerificationAccount, JobAccount, JobPost) с примерами
- [ ] Разработать скрипт миграции данных из существующих файлов (Job_Account_prod.json, Account_prod.md, LeadAccount clusters) в новую структуру
- [ ] Спроектировать систему фильтрации с индексами и query builder для удобного поиска аккаунтов по различным критериям
- [ ] Создать спецификацию API endpoints для работы с аккаунтами, включая фильтрацию, верификацию и управление вакансиями
- [ ] Реализовать схему шифрования паролей и OAuth токенов, систему ролей и прав доступа