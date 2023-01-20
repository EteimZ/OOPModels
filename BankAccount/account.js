class AccountBase {
    #account_name
    #bank_name
    #balance
    #created
    #updated

    constructor(account_name, bank_name, balance = 0) {
        if (new.target === AccountBase) {
            throw new Error("Cannot instantiate abstract class Animal directly")
        }
        this.#account_name = account_name
        this.#bank_name = bank_name
        this.#balance = balance
        this.#created = new Date()
        this.#updated = null
    }

    withdraw(amount) {
        if (this.#balance >= amount) {
            this.#balance -= amount;
            this.#created = new Date()
            console.log(console.log(`Detail: ₦${amount} succesfully withdrawn.`))
        } else {
            console.log("Withdrawal failed")
        }
    }

    deposit() {
        throw new Error("Must be implemented by a subclass");
    }

    balances() {
        return this.#balance
    }

    info() {
        console.log(`Bank name: ${this.#bank_name}`)
        console.log(`Account name: ${this.#account_name}`)
        console.log(`Account balance: ₦ ${this.#balance}`)
        console.log(`Account created at: ${this.#created}`)
        console.log(`Account updated at: ${this.#updated}`)
    }
}

class AdultAccount extends AccountBase {

    deposit(amount) {
        this.balance += amount
        this.created = new Date()
        console.log("Deposit succesful")
    }
}

class StudentAccount extends AccountBase {

    static ACCOUNT_LIMIT = 4E5;


    deposit(amount) {
        if ((this.balance + amount > this.ACCOUNT_LIMIT)) {
            console.log("Account limit exceeded.")
        } else {
            this.balance += amount
            this.created = new Date()
            console.log("Deposit succesful")
        }

    }
}

class Bank {
    #name
    #accounts

    constructor(name) {
        this.#name = name
        this.#accounts = []
    }

    create_adult_account(account_name, initial_deposit) {
        const acct = new AdultAccount(account_name, this.#name, initial_deposit)
        this.#accounts.push(acct)
        return acct
    }

    list_accounts() {
        return this.#accounts
    }

    total_amount() {
        const total = this.#accounts.reduce((sum, acct) => sum + acct.balances(), 0);
        return total
    }
}

if (require.main === module) {
    const b = new Bank(name = "ebank");
    const acct1 = b.create_adult_account(account_name = "Diseyi", initial_deposit = 40000)
    const acct2 = b.create_adult_account(account_name = "Philomena", initial_deposit = 4000)

    b.list_accounts().forEach(item => item.info())

    console.log(`Bank total balance: ${b.total_amount()}`)
    acct1.deposit(8000)
    console.log(`Bank total balance: ${b.total_amount()}`)
}