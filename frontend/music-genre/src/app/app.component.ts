import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Audio Genre Classifier';
  selectedFile: File | null = null;
  predictionResult: string = '';
  isLoading: boolean = false;

  constructor(private http: HttpClient) { }

  onFileSelected(event: any) {
    this.selectedFile = event.target.files[0];
  }

  testWithSVM() {
    if (!this.selectedFile) {
      alert('Please select a file first.');
      return;
    }

    this.isLoading = true;
    const formData = new FormData();
    formData.append('file', this.selectedFile);

    this.http.post<any>('http://localhost:5001/predict', formData).subscribe({
      next: (response) => {
        this.predictionResult = `SVM Predicted Genre: ${response.predicted_genre}`;
        this.isLoading = false;
      },
      error: (err) => {
        console.error(err);
        this.predictionResult = 'Error with SVM prediction.';
        this.isLoading = false;
      }
    });
  }

  testWithVGG() {
    if (!this.selectedFile) {
      alert('Please select a file first.');
      return;
    }

    this.isLoading = true;
    const formData = new FormData();
    formData.append('file', this.selectedFile);

    this.http.post<any>('http://localhost:5002/predict', formData).subscribe({
      next: (response) => {
        this.predictionResult = `VGG Predicted Genre: ${response.predicted_genre}`;
        this.isLoading = false;
      },
      error: (err) => {
        console.error(err);
        this.predictionResult = 'Error with VGG prediction.';
        this.isLoading = false;
      }
    });
  }
}
