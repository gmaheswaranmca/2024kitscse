import { Component } from '@angular/core';

@Component({
  selector: 'app-calc',
  templateUrl: './calc.component.html',
  styleUrl: './calc.component.css'
})
export class CalcComponent {
  num = 15
  res = 0
  findSquare(){
    this.res = this.num * this.num
  }
}
