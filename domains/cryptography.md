# Introduction to cryptography

Last reviewed: 2026-10-03

Cryptography is the use of mathematics to protect information. It keeps data secret, proves that data has not been changed and proves who sent it. Almost everything else in security depends on it: the padlock in your browser, password storage, secure messaging, software updates and cloud encryption keys.

Most people in security never design cryptography. They choose it, use it and find places where it was used badly. That is the skill to aim for.

## Why it matters

When cryptography is used correctly, it protects data even if an attacker gets hold of it. When it is used badly, it gives a false sense of safety. Many real breaches involve passwords stored with a weak method, keys left in source code or certificates that nobody checked.

## Key ideas

Learn these four tools and the problem each one solves.

| Goal | Tool | How it works | Examples |
|---|---|---|---|
| Keep data secret | Symmetric encryption | One shared key encrypts and decrypts. Fast, used for bulk data | AES, ChaCha20 |
| Share a key or prove identity without a shared secret | Asymmetric encryption | A key pair: a public key anyone can have and a private key you keep | RSA, elliptic curve schemes such as Ed25519 |
| Detect changes | Hash function | Turns any input into a fixed-length fingerprint. One way, and a tiny change gives a completely different result | SHA-256, SHA-3 |
| Prove who sent it | Digital signature | You sign with your private key. Anyone can verify with your public key | Ed25519, RSA signatures |

Other ideas to know:

- **Encoding is not encryption.** Base64 only changes the format. Anyone can reverse it.
- **Hashing is not encryption.** You cannot turn a hash back into the original.
- **Password storage.** Store passwords with a slow, salted hashing method designed for the job, such as Argon2id, bcrypt or scrypt. A fast hash such as plain SHA-256 can be guessed at billions of tries a second.
- **Message authentication codes (HMAC).** Prove a message came from someone who has a shared key and was not changed.
- **Certificates and PKI.** A certificate ties a public key to a name, and a certificate authority signs it. Your browser trusts a site because a trusted authority vouched for its certificate.
- **TLS.** The protocol behind HTTPS. It uses asymmetric methods to agree a key and then symmetric encryption to protect the traffic.
- **Key management.** The hardest part. Keys must be generated well, stored safely, rotated and destroyed. Cloud key management services and hardware security modules exist for this.
- **Randomness.** Keys and nonces need a cryptographically secure random number generator, not an ordinary one.

Old algorithms fail over time. MD5 and SHA-1 are broken for security use. A large enough quantum computer could break RSA and elliptic curve methods, so standards bodies are preparing replacements. Status as of October 2026, from [NIST's post-quantum page](https://csrc.nist.gov/pqc-standardization): on 13 August 2024 NIST published its first three post-quantum standards. FIPS 203 (ML-KEM) is for establishing keys. FIPS 204 (ML-DSA) and FIPS 205 (SLH-DSA) are for digital signatures. A fourth, FIPS 206 for the FALCON signature scheme, is still in development, and in March 2025 NIST selected HQC as a backup method for key establishment. Many organisations are now planning their migration. Check NIST's page for the current state, because this area is moving.

## What people in this field do

- Security engineers choose algorithms and libraries, design how keys are stored and rotated, and set up certificates.
- Application security engineers and penetration testers look for weak password storage, bad randomness, missing encryption and certificate checks that were switched off.
- Researchers and cryptographers design and break algorithms. This is a small field and needs a strong mathematics background.
- Compliance staff check that encryption requirements in standards such as PCI DSS and the NDPA's security rules are met.

## Common tools

| Tool | What it does |
|---|---|
| [OpenSSL](https://www.openssl.org/) | Command-line tool for hashes, keys, signatures and certificates |
| [GnuPG](https://gnupg.org/) | Encrypts and signs files and email |
| [CyberChef](https://gchq.github.io/CyberChef/) | Decode, hash and transform data in a browser |
| [John the Ripper](https://www.openwall.com/john/) and [hashcat](https://hashcat.net/hashcat/) | Test how quickly password hashes can be guessed. Use them only on hashes you made |
| [Qualys SSL Labs](https://www.ssllabs.com/ssltest/) | Grades the TLS setup of a public website |

## Try it in your lab

1. Hash a short text with `sha256sum`. Change one letter and hash it again. Compare the results.
2. Encrypt a file with `gpg --symmetric --cipher-algo AES256 secret.txt` and decrypt it again. Try the wrong passphrase.
3. With OpenSSL 3, create a key pair, sign a file and verify the signature. Then change one byte of the file and verify again.

   ```
   openssl genpkey -algorithm ed25519 -out key.pem
   openssl pkey -in key.pem -pubout -out pub.pem
   openssl pkeyutl -sign -inkey key.pem -rawin -in message.txt -out message.sig
   openssl pkeyutl -verify -pubin -inkey pub.pem -rawin -in message.txt -sigfile message.sig
   ```

4. Look at a website's certificate:

   ```
   openssl s_client -connect example.com:443 -servername example.com </dev/null | openssl x509 -noout -subject -issuer -dates
   ```

   Say who issued it, who it was issued to and when it expires.
5. Create MD5 and bcrypt hashes of three weak passwords you choose. Try to crack them with John the Ripper and a small word list. Compare how long each takes.

## Mistakes beginners make and attackers look for

- Writing your own encryption instead of using a reviewed library
- Hard-coding keys and passwords in source code
- Using MD5 or SHA-1 for passwords or signatures
- Encrypting without authentication, so changes are not detected
- Reusing a nonce or initialisation vector
- Using ECB mode, which shows patterns in the data
- Clicking through certificate warnings in code or in the browser

## Practice

- [CryptoHack](https://cryptohack.org/), a free site of cryptography challenges with explanations
- [Cryptopals](https://cryptopals.com/), a set of practical exercises that build up to real attacks
- [OverTheWire Krypton](https://overthewire.org/wargames/krypton/), classical ciphers in a terminal game
- The cryptography challenges in [picoCTF](https://picoctf.org/)

## Where to go next

- A free book for programmers: [Crypto 101](https://www.crypto101.io/)
- Roles: [Security Engineer (Software)](../careers/security-engineer-software.md), [Security Researcher](../careers/security-researcher.md), [Application Security Expert](../careers/application-security-expert.md)
- Libraries and tools by language: [reference: cryptography](../reference/cryptography.md)
- Related guides: [network security basics](../guides/network-security-basics.md) for TLS and VPNs, and the [glossary](../guides/glossary.md)
