export class ComplexNumber {
  constructor(public readonly real: number, public readonly imag: number) {}

  get abs(): number {
    return Math.sqrt(this.real ** 2 + this.imag ** 2);
  }

  get conj(): ComplexNumber {
    return new ComplexNumber(this.real, this.imag === 0 ? 0 : -this.imag);
  }

  get exp(): ComplexNumber {
    const eRaisedToReal = Math.exp(this.real);
    return new ComplexNumber(
      eRaisedToReal * Math.cos(this.imag),
      eRaisedToReal * Math.sin(this.imag)
    );
  }

  add(num: ComplexNumber): ComplexNumber {
    return new ComplexNumber(this.real + num.real, this.imag + num.imag);
  }

  sub(num: ComplexNumber): ComplexNumber {
    return new ComplexNumber(this.real - num.real, this.imag - num.imag);
  }

  mul(num: ComplexNumber): ComplexNumber {
    return new ComplexNumber(
      this.real * num.real - this.imag * num.imag,
      this.real * num.imag + this.imag * num.real
    );
  }

  div(num: ComplexNumber): ComplexNumber {
    const denominator = num.real ** 2 + num.imag ** 2;
    return new ComplexNumber(
      (this.real * num.real + this.imag * num.imag) / denominator,
      (this.imag * num.real - this.real * num.imag) / denominator
    );
  }
}
