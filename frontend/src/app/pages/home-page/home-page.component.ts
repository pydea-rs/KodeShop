import { Component } from '@angular/core';
import { SliderComponent } from './slider/slider.component';
import { LogosComponent } from '../../sections/logos/logos.component';

@Component({
  selector: 'app-home-page',
  standalone: true,
  imports: [SliderComponent, LogosComponent],
  templateUrl: './home-page.component.html',
  styleUrl: './home-page.component.scss'
})
export class HomePageComponent {

}
