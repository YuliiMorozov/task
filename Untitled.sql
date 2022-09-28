CREATE TABLE "WaterInvoice" (
  "id" SERIAL PRIMARY KEY,
  "count" float8
);

CREATE TABLE "GasInvoice" (
  "id" SERIAL PRIMARY KEY,
  "count" float8
);

CREATE TABLE "ElectricityInvoice" (
  "id" SERIAL PRIMARY KEY,
  "count" float8
);

CREATE TABLE "Invoice" (
  "id" SERIAL PRIMARY KEY,
  "flat_id" int,
  "water_invoice_id" int,
  "gas_invoice_id" int,
  "electricity_invoice_id" int,
  "date" datetime
);

CREATE TABLE "House" (
  "id" SERIAL PRIMARY KEY,
  "house_number" int
);

CREATE TABLE "Flat" (
  "id" SERIAL PRIMARY KEY,
  "house_id" int,
  "flat_number" int
);

ALTER TABLE "Flat" ADD FOREIGN KEY ("house_id") REFERENCES "House" ("id");

ALTER TABLE "Invoice" ADD FOREIGN KEY ("flat_id") REFERENCES "Flat" ("id");

ALTER TABLE "WaterInvoice" ADD FOREIGN KEY ("id") REFERENCES "Invoice" ("water_invoice_id");

ALTER TABLE "GasInvoice" ADD FOREIGN KEY ("id") REFERENCES "Invoice" ("gas_invoice_id");

ALTER TABLE "ElectricityInvoice" ADD FOREIGN KEY ("id") REFERENCES "Invoice" ("electricity_invoice_id");
